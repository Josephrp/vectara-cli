# ./vectara-cli/advanced/nerdspan.py

import spacy
from span_marker import SpanMarkerModel
from vectara_cli.core import VectaraClient
import json
import logging
from vectara_cli.data.corpus_data import CorpusData
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

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

    def create_corpus(self, name, description):
        logging.info(f"Creating corpus with name: {name}")
        corpus_data = CorpusData(
            name=name,
            description=description,
            enabled=True,
            swapQenc=False,
            swapIenc=False,
            textless=False,
            encrypted=False,
            encoderId=1,
            metadataMaxBytes=10000,
            customDimensions=[],
            filterAttributes=[],
        ).to_dict()
        response = self.vectara_client.create_corpus(corpus_data)
        logging.info(f"Corpus creation response: {response}")
        return response

    def text_chunker(self, text, chunk_size=512):
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def process_and_upload(self, folder_path, model_name, model_type):
        logging.info("Starting the processing and upload of documents.")
        corpus_response_1 = self.create_corpus("Corpus 1", "First corpus for raw uploads")
        corpus_id_1 = corpus_response_1['data']['corpusId'] 
        corpus_response_2 = self.create_corpus("Corpus 2", "Second corpus for processed uploads") 
        corpus_id_2 = corpus_response_2['data']['corpusId'] 

        upload_results = self.vectara_client.index_documents_from_folder(
            corpus_id_1, folder_path, return_extracted_document=True
        )

        for document_id, success, extracted_text in upload_results:
            logging.info(f"Processing document {document_id}...")
            if not success or extracted_text is None:
                logging.warning(f"Skipping document {document_id}, upload failed or no text extracted.")
                continue

            chunks = self.text_chunker(extracted_text)
            # self.load_model(model_name, model_type)
            logging.info(f"Analyzing chunk for document {document_id}...")
            for chunk in chunks:
                self.text = chunk
                _, key_value_pairs = self.analyze_text()
                metadata_json = json.dumps({"entities": key_value_pairs})
                self.vectara_client.index_text(
                    corpus_id=corpus_id_2, document_id=document_id, text=chunk, metadata_json=metadata_json
                )

        logging.info("Finished processing and uploading documents.")
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