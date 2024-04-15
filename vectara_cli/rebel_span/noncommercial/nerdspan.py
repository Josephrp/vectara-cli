# ./vectara-cli/advanced/nerdspan.py

import spacy
from span_marker import SpanMarkerModel
from vectara_cli.core import VectaraClient
import json
import logging


class Span:
    def __init__(self, vectara_client, text, model_name, model_type):
        self.text = text
        self.vectara_client = vectara_client
        self.model_name = model_name
        self.model_type = model_type
        self.models = {}
        
        self.model_mapping = {
            "fewnerdsuperfine": "tomaarsen/span-marker-bert-base-fewnerd-fine-super",
            "multinerd": "tomaarsen/span-marker-mbert-base-multinerd",
            "largeontonote": "tomaarsen/span-marker-roberta-large-ontonotes5"
        }
        self.load_model()


    def load_model(self):
        full_model_name = self.model_mapping.get(self.model_name)
        if not full_model_name:
            logging.error("Model name '%s' is not recognized.", self.model_name)
            raise ValueError(f"Model '{self.model_name}' not recognized.")
        if self.model_type == "span_marker":
            try:
                self.models[self.model_name] = SpanMarkerModel.from_pretrained(full_model_name)
            except Exception as e:
                logging.error("Failed to load model '%s' due to: %s", full_model_name, e)
                raise
        elif self.model_type == "spacy":
            try:
                self.models[self.model_name] = spacy.load("en_core_web_sm")
            except Exception as e:
                logging.error("Failed to load spacy model due to: %s", e)
                raise
        else:
            logging.error("Unsupported model type: %s", self.model_type)
            raise ValueError("Unsupported model type")

    def run_inference(self):
        model = self.models.get(self.model_name)
        if not model:
            logging.error("Model not found for: %s", self.model_name)
            raise ValueError("Model not loaded")
        try:
            if hasattr(model, 'predict'):
                results = model.predict(self.text)
                logging.debug("Model predictions: %s", results)
                return results
            else:
                results = [(ent.text, ent.label_) for ent in model(self.text).ents]
                logging.debug("Spacy entities extracted: %s", results)
                return results
        except Exception as e:
            logging.error("Inference failed due to: %s", e)
            raise

    def format_output(self, entities):
        output_str = f"Entities found in the text: {self.text}\n"
        key_value_pairs = [{'span': ent[0], 'label': ent[1]} for ent in entities]
        output_str += '\n'.join([f"{kv['span']} ({kv['label']})" for kv in key_value_pairs])
        return output_str, key_value_pairs

    def analyze_text(self):
        entities = self.run_inference()
        output_str = f"Entities found in the text: {self.text}\n"
        key_value_pairs = [{'span': ent['span'], 'label': ent['label'], 'score': ent['score']} for ent in entities]
        output_str += "\n".join([f"{kvp['span']} ({kvp['label']} - Score: {kvp['score']:.2f})" for kvp in key_value_pairs])
        return output_str, key_value_pairs

    def create_corpus(self, description):
#       corpus_id = uuid.uuid4().int  # Generates a random corpus ID
        response = self.vectara_client.create_corpus(
 #          corpus_id=corpus_id,
 #          name=name,
            description=description,
#           dtProvision=int(uuid.uuid1().time),  # Example timestamp
            enabled=True,
            swapQenc=False,
            swapIenc=False,
            textless=False,
            encrypted=False,
            encoderId="default",
            metadataMaxBytes=10000,
            customDimensions=[],
            filterAttributes=[],
        )
        print(f"Corpus creation response: {response}")
        return corpus_id

    def text_chunker(self, text, chunk_size=512):
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def process_and_upload(self, folder_path, model_name, model_type):
        # Create two corpora
        corpus_id_1 = self.create_corpus("Corpus 1", "First corpus for raw uploads")
        corpus_id_2 = self.create_corpus(
            "Corpus 2", "Second corpus for processed uploads"
        )

        # Upload documents from folder to the first corpus
        upload_results = self.vectara_client.index_documents_from_folder(
            corpus_id_1, folder_path, return_extracted_document=True
        )

        for document_id, success, extracted_text in upload_results:
            if not success or extracted_text is None:
                print(
                    f"Skipping document {document_id}, upload failed or no text extracted."
                )
                continue

            # Chunk the text
            chunks = self.text_chunker(extracted_text)

            # Process each chunk and re-upload to the second corpus
            self.load_model()
            for chunk in chunks:
                self.text = chunk  # Update the Span text to the current chunk
                _, key_value_pairs = self.analyze_text(model_name)
                # Convert key-value pairs to a metadata JSON string
                metadata_json = json.dumps({"entities": key_value_pairs})
                # Index processed chunk into the second corpus
                self.vectara_client.index_text(
                    corpus_id_2, document_id, chunk, metadata_json=metadata_json
                )

        return corpus_id_1, corpus_id_2
    
    
# class Span:
#     """
#     Model Name and model

#     ```
#     self.model_mapping = {
#             "fewnerdsuperfine": "tomaarsen/span-marker-bert-base-fewnerd-fine-super",
#             "multinerd": "tomaarsen/span-marker-mbert-base-multinerd",
#             "largeontonote": "tomaarsen/span-marker-roberta-large-ontonotes5",
#         }
#     ```
#     Model Types
#     -------
#     - span_marker
#     - spacy
#     """    