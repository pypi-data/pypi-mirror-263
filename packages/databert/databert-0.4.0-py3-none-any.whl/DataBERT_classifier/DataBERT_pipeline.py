from transformers import BertForSequenceClassification, BertTokenizer
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler, TensorDataset
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import torch
import numpy as np
import tempfile
from huggingface_hub import HfFolder, Repository
import os
from sklearn.metrics import roc_auc_score
import copy
import tempfile
import requests
import PyPDF2
from nltk.tokenize import sent_tokenize
from tqdm.auto import tqdm
import datasets

# ================ FINE-TUNE BERT ======================


class TrainBERTClassifier:
    def __init__(
        self,
        model_name="bert-base-uncased",
        num_labels=2,
        max_length=32,
        batch_size=16,
        learning_rate=5e-5,
        epsilon=1e-8,
        epochs=2000,
        patience=3,
        tolerance=1e-4,
    ):

        self.patience = patience
        self.tolerance = tolerance
        self.best_val_roc_auc = 0.0  # Initialize the best ROC-AUC score
        self.epochs_no_improve = 0  # Initialize the count for epochs without improvement
        self.best_model_state = None

        """
        Initializes the BERT Classifier for training and evaluation.

        Args:
        model_name (str): Name or path of the pre-trained model.
        num_labels (int): Number of labels for classification.
        max_length (int): Maximum length of the input sequence.
        batch_size (int): Batch size for training and evaluation.
        learning_rate (float): Learning rate for the optimizer.
        epsilon (float): Epsilon value for the optimizer.
        epochs (int): Number of training epochs.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = BertForSequenceClassification.from_pretrained(
            model_name, num_labels=num_labels
        ).to(self.device)
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.max_length = max_length
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.epochs = epochs

    def preprocess(self, texts):
        """
        Preprocesses a list of texts for BERT model.

        Args:
        texts (list of str): List of texts to be preprocessed.

        Returns:
        TensorDataset: A dataset of input IDs and attention masks.
        """
        input_ids = []
        attention_masks = []

        for text in texts:
            encoding = self.tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=self.max_length,
                padding="max_length",
                truncation=True,
                return_attention_mask=True,
                return_tensors="pt",
            )
            input_ids.append(encoding["input_ids"])
            attention_masks.append(encoding["attention_mask"])
        input_ids = torch.cat(input_ids, dim=0)
        attention_masks = torch.cat(attention_masks, dim=0)

        return TensorDataset(input_ids, attention_masks)

    @staticmethod
    def flat_accuracy(preds, labels):
        """
        Calculates the accuracy of the predictions based on the comparison with true labels.

        Args:
        preds: Numpy array of predictions.
        labels: Numpy array of actual labels.

        Returns:
        float: Accuracy score.
        """
        pred_flat = np.argmax(preds, axis=1).flatten()
        labels_flat = labels.flatten()
        return np.sum(pred_flat == labels_flat) / len(labels_flat)

    def b_tp(self, preds, labels):
        """
        Calculates the number of true positives.

        Args:
        preds (list or array): Predicted labels.
        labels (list or array): Actual labels.

        Returns:
        int: Number of true positives.
        """
        return sum((pred == 1) and (label == 1) for pred, label in zip(preds, labels))

    def b_fp(self, preds, labels):
        """
        Calculates the number of false positives.

        Args:
        preds (list or array): Predicted labels.
        labels (list or array): Actual labels.

        Returns:
        int: Number of false positives.
        """
        return sum((pred == 1) and (label == 0) for pred, label in zip(preds, labels))

    def b_tn(self, preds, labels):
        """
        Calculates the number of true negatives.

        Args:
        preds (list or array): Predicted labels.
        labels (list or array): Actual labels.

        Returns:
        int: Number of true negatives.
        """
        return sum((pred == 0) and (label == 0) for pred, label in zip(preds, labels))

    def b_fn(self, preds, labels):
        """
        Calculates the number of false negatives.

        Args:
        preds (list or array): Predicted labels.
        labels (list or array): Actual labels.

        Returns:
        int: Number of false negatives.
        """
        return sum((pred == 0) and (label == 1) for pred, label in zip(preds, labels))

    def b_metrics(self, preds, labels):
        """
        Calculates binary classification metrics including accuracy, precision, recall, and specificity.

        Args:
        preds (array): Model's probability predictions before applying threshold.
        labels (array): Actual labels.

        Returns:
        tuple: A tuple containing the accuracy, precision, recall, and specificity.
        """
        preds = np.argmax(preds, axis=1).flatten()
        labels = labels.flatten()

        tp = self.b_tp(preds, labels)
        tn = self.b_tn(preds, labels)
        fp = self.b_fp(preds, labels)
        fn = self.b_fn(preds, labels)

        b_accuracy = (tp + tn) / len(labels)
        b_precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        b_recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        b_specificity = tn / (tn + fp) if (tn + fp) > 0 else 0

        return b_accuracy, b_precision, b_recall, b_specificity
    
    def compute_roc_auc(self, preds, labels):
        """
        Computes the ROC-AUC score.

        Args:
        preds (np.array): Raw model predictions (logits or probabilities).
        labels (np.array): Actual labels.

        Returns:
        float: ROC-AUC score.
        """
        # Convert softmax output to positive class probabilities for ROC-AUC calculation
        preds_proba = np.exp(preds)[:, 1] / np.sum(np.exp(preds), axis=1)
        roc_auc = roc_auc_score(labels, preds_proba)
        return roc_auc

    def train(self, train_texts, train_labels, val_texts, val_labels):
        """
        Trains and evaluates the BERT model.

        Args:
        train_texts (list of str): Training texts.
        train_labels (list of int): Training labels.
        val_texts (list of str): Validation texts.
        val_labels (list of int): Validation labels.
        """
        train_dataset = self.preprocess(train_texts)
        val_dataset = self.preprocess(val_texts)

        train_labels = torch.tensor(train_labels)
        val_labels = torch.tensor(val_labels)

        train_dataset = TensorDataset(
            train_dataset.tensors[0], train_dataset.tensors[1], train_labels
        )
        val_dataset = TensorDataset(
            val_dataset.tensors[0], val_dataset.tensors[1], val_labels
        )

        train_dataloader = DataLoader(
            train_dataset,
            sampler=RandomSampler(train_dataset),
            batch_size=self.batch_size,
        )
        validation_dataloader = DataLoader(
            val_dataset,
            sampler=SequentialSampler(val_dataset),
            batch_size=self.batch_size,
        )

        optimizer = torch.optim.AdamW(
            self.model.parameters(), lr=self.learning_rate, eps=self.epsilon
        )

        for epoch in range(self.epochs):
            self.model.train()
            total_loss = 0

            for batch in train_dataloader:
                batch = tuple(b.to(self.device) for b in batch)
                b_input_ids, b_input_mask, b_labels = batch
                self.model.zero_grad()
                outputs = self.model(
                    b_input_ids,
                    token_type_ids=None,
                    attention_mask=b_input_mask,
                    labels=b_labels,
                )
                loss = outputs.loss
                total_loss += loss.item()
                loss.backward()
                optimizer.step()
            avg_train_loss = total_loss / len(train_dataloader)
            print(f"Epoch {epoch + 1}")
            print(f"Training loss: {avg_train_loss}")

            self.model.eval()
            eval_accuracy = 0
            eval_metrics = np.zeros(
                4
            )  # To store accuracy, precision, recall, specificity
            nb_eval_steps = 0

            logits_all = []
            label_ids_all = []

            for batch in validation_dataloader:
                batch = tuple(b.to(self.device) for b in batch)
                b_input_ids, b_input_mask, b_labels = batch

                with torch.no_grad():
                    outputs = self.model(
                        b_input_ids, token_type_ids=None, attention_mask=b_input_mask
                    )
                logits = outputs.logits.detach().cpu().numpy()
                label_ids = b_labels.to("cpu").numpy()

                logits_all.append(logits)
                label_ids_all.append(label_ids)

                tmp_eval_accuracy = self.flat_accuracy(logits, label_ids)
                eval_accuracy += tmp_eval_accuracy
                metrics = self.b_metrics(logits, label_ids)
                eval_metrics += np.array(metrics)
                nb_eval_steps += 1

            # Concatenate all logits and labels from the validation loop
            logits_all = np.concatenate(logits_all, axis=0)
            label_ids_all = np.concatenate(label_ids_all, axis=0)

            # Compute ROC-AUC after processing all validation batches
            roc_auc = self.compute_roc_auc(logits_all, label_ids_all)
            print(f"Validation ROC-AUC: {roc_auc}")
            print(f"Validation Accuracy: {eval_accuracy / nb_eval_steps}")
            print(f"Validation Precision: {eval_metrics[1] / nb_eval_steps}")
            print(f"Validation Recall: {eval_metrics[2] / nb_eval_steps}")
            print(f"Validation Specificity: {eval_metrics[3] / nb_eval_steps}")


            if roc_auc > self.best_val_roc_auc + self.tolerance:
                self.best_val_roc_auc = roc_auc
                self.epochs_no_improve = 0
                self.best_model_state = copy.deepcopy(self.model.state_dict())  # Save the best model state
            else:
                self.epochs_no_improve += 1
                print(f"No improvement in validation ROC-AUC for {self.epochs_no_improve} consecutive epochs.")

                if self.epochs_no_improve >= self.patience:
                    print("Early stopping triggered.")
                    if self.best_model_state is not None:
                        print("Restoring best model weights!")
                        self.model.load_state_dict(self.best_model_state)  # Restore the best model state
                    break


    def save_model_and_tokenizer(self, save_directory):
        """
        Saves the trained model and tokenizer to the specified directory.

        Args:
        save_directory (str): The directory to save the model and tokenizer.
        """
        # Ensure the save directory exists
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Save the model
        model_save_path = os.path.join(save_directory, "model")
        self.model.save_pretrained(model_save_path)

        # Save the tokenizer
        tokenizer_save_path = os.path.join(save_directory, "tokenizer")
        self.tokenizer.save_pretrained(tokenizer_save_path)

        print(f"Model and tokenizer saved in {save_directory}")

    def push_to_huggingface_hub(self, commit_message="Push model to Hugging Face Hub"):
        """
        Pushes the fine-tuned model to the Hugging Face Hub, prompting the user for their username and access token.

        Args:
        commit_message (str): Commit message for the repository.
        """
        # Prompt the user for their Hugging Face username and access token

        hf_username = input("Enter your Hugging Face username: ")
        hf_access_token = input("Enter your Hugging Face access token: ")

        # Create a temporary directory to store model files

        temp_dir = tempfile.mkdtemp()

        # Save the model to the temporary directory

        self.model.save_pretrained(temp_dir)

        # Define the desired model name on the Hugging Face Hub

        model_name_on_hub = input("Enter your desired model name on Hugging Face Hub: ")

        # Initialize a repository in the temporary directory, set to push to the Hugging Face Hub

        repo = Repository(
            local_dir=temp_dir,
            clone_from=f"{hf_username}/{model_name_on_hub}",
            use_auth_token=hf_access_token,
        )

        # Push the model to the Hugging Face Hub

        repo.push_to_hub(commit_message=commit_message)


# =================== CLASSIFYING WITH TRAINED MODEL ====================


class BERTClassifier:
    def __init__(
        self, model_path="jamesliounis/DataBERT", tokenizer_name="bert-base-uncased"
    ):
        """
        Initializes the BERT Classifier with the fine-tuned model and tokenizer.

        Args:
        model_path (str): Path to the fine-tuned model directory.
        In this case, points to HuggingFace where we have deployed the fine-tuned model.
        tokenizer_name (str): Pretrained tokenizer name or path.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = BertForSequenceClassification.from_pretrained(model_path).to(
            self.device
        )
        self.tokenizer = BertTokenizer.from_pretrained(tokenizer_name)

    def preprocess(self, input_text):
        """
        Preprocesses the input text for BERT model.

        Args:
        input_text (str): Text to be preprocessed.

        Returns:
        torch.Tensor: Tensor of token IDs.
        torch.Tensor: Tensor of attention masks.
        """
        encoding = self.tokenizer.encode_plus(
            input_text,
            add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
            max_length=32,  # Pad & truncate all sentences.
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            return_tensors="pt",  # Return PyTorch tensors
        )

        input_ids = encoding["input_ids"].to(self.device)
        attention_mask = encoding["attention_mask"].to(self.device)

        return input_ids, attention_mask

    def predict(self, input_text):
      """
      Generates predictions and confidence scores for the input text.

      Args:
      input_text (str): Text to generate prediction for.

      Returns:
      str: Predicted class ('Contains dataset mention' or 'Does not contain dataset mention').
      float: Confidence score for the prediction.
      """
      self.model.eval()

      input_ids, attention_mask = self.preprocess(input_text)

      with torch.no_grad():
          outputs = self.model(input_ids, attention_mask=attention_mask)
      logits = outputs.logits
      probabilities = F.softmax(logits, dim=1)
      predicted_class_id = logits.argmax().item()
      confidence = probabilities[0, predicted_class_id].item()

      return (
          # Binary classification
          1
          if predicted_class_id == 1
          else 0,
          # Confidence score
          confidence
      )



    # ============= DOCUMENT PROCESSING =============

    class DocumentProcessor:

        def __init__(
            self, organization, json_cache_dir, tokenizer_model="bert-base-uncased"
        ):
            """
            Initializes the DocumentProcessor with a specific tokenizer model and organization details.

            Args:
            organization (str): Name of the organization for dataset pushing.
            json_cache_dir (str): Directory to cache processed documents.
            tokenizer_model (str): Pretrained BERT tokenizer model.
            """
            self.organization = organization  # Organization name for dataset publishing.
            self.json_cache_dir = json_cache_dir  # Directory to store cached documents.
            # Initialize a BERT tokenizer for text processing.
            self.tokenizer = BertTokenizer.from_pretrained(
                tokenizer_model, do_lower_case=True
            )

        def extract_text(self, pdf_path, mode):
            """
            Extracts text from a PDF file, either in chunks (full page) or by sentences.

            Args:
            pdf_path (str): Path to the PDF file to be processed.
            mode (str): The mode of text extraction - 'chunk' for page-wise, 'sent' for sentence-wise.

            Returns:
            list: A list of extracted text chunks or sentences.
            """
            content = []
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                # Iterate through PDF pages.
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()  # Extract text from the current page.
                    if mode == "chunk":
                        content.append(text)  # Append the whole text as one chunk.
                    elif mode == "sent":
                        # Tokenize and append each sentence separately.
                        sentences = sent_tokenize(text)
                        content.extend(sentences)
            return content

        def get_doc_from_url(self, pdf_url, mode="chunk"):
            """
            Downloads a PDF document from a given URL and extracts text based on the specified mode.

            Args:
            pdf_url (str): URL of the PDF to download and process.
            mode (str): The mode of text extraction - 'chunk' or 'sent'.

            Returns:
            list: A list of extracted text chunks or sentences.

            Raises:
            Exception: If there is an issue with downloading the PDF.
            """
            with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_pdf:
                response = requests.get(pdf_url, stream=True)
                if response.status_code == 200:
                    # Write the content of the PDF to a temporary file.
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            temp_pdf.write(chunk)
                    temp_pdf.seek(0)  # Reset file pointer.
                    # Extract text from the downloaded PDF.
                    return self.extract_text(temp_pdf.name, mode)
                else:
                    raise Exception(
                        f"Error downloading the file: Status code {response.status_code}"
                    )

        def create_dataset(self, documents, mode="chunk"):
            """
            Creates and pushes a dataset from a list of document contents to Hugging Face Hub.

            Args:
            documents (list): List of document contents to be included in the dataset.
            mode (str): Mode of dataset creation, can be 'chunk' or 'sent'.

            Raises:
            AssertionError: If the mode is not 'chunk' or 'sent'.
            """
            assert mode in ["chunk", "sent"]

            dataset = {}
            # Construct the dataset from document contents.
            for i, content in enumerate(tqdm(documents)):
                dataset[i] = {"content": content}

            # Create and push the dataset to Hugging Face Hub.
            data = datasets.Dataset.from_dict(dataset)
            data.push_to_hub(
                f"{self.organization}/wb-prwp-{mode}",
                private=True,
                commit_message=f"Add {mode} new dataset.",
            )

        def classify(self, documents):
            """
            Classifies a list of documents using a fine-tuned BERT model.
            Pipeline is in separate file: DataBERT_pipeline.py

            Args:
            model_path (str): Path to the fine-tuned BERT model directory.
            documents (list of str): Documents to classify.
            Note: In our case, we apply the function directly to individual sentences.
            The iterative approach just further enforces modularity that we may need in future versions.

            Returns:
            list: A list containing classification results for each document.
            """
            bert_classifier = (
                BERTClassifier()
            )  # Initialize the BertClassifier with the fine-tuned model.
            classifications = []

            # Iterate over all documents and predict their classes.
            for doc in tqdm(documents, desc="Classifying documents"):
                classification = bert_classifier.predict(doc)
                classifications.append(classification)

            return classifications



