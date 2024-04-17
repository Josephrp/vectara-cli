# ./advanced/commercial/enterpise.py

import logging
from typing import List, Any, Dict
from vectara_cli.core import VectaraClient
import span_marker
from span_marker import SpanMarkerModel
import random
import string
import json

class EnterpriseSpan:
    """
    EnterpriseSpan class for handling advanced text processing and analysis in enterprise applications.
    This class wraps around the SpanMarkerModel for keyphrase extraction and adds enterprise-level features
    such as detailed logging, error handling, and customization options, including an easy way to specify models.
    """

    MODEL_MAP = {
        "keyphrase": "tomaarsen/span-marker-bert-base-uncased-keyphrase-inspec",
        "science": "tomaarsen/span-marker-bert-base-ncbi-disease",
    }

    def __init__(self, model_name: str):
        """
        Initializes the EnterpriseSpan model with a given model name.

        Parameters:
            model_name (str): User-friendly name or identifier for the pretrained model.
        """
        self.model_name = model_name
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model_path = self._get_model_path()
        self.model = self._load_model()
        self.vectara_client = VectaraClient()

    def _get_model_path(self) -> str:
        """
        Translates the user-friendly model name to its specific identifier.

        Returns:
            str: The model identifier.
        """
        if self.model_name in self.MODEL_MAP:
            return self.MODEL_MAP[self.model_name]
        else:
            self.logger.warning(
                f"Model name {self.model_name} not recognized. Attempting to use it as a direct path or identifier."
            )
            return self.model_name

    def _load_model(self) -> SpanMarkerModel:
        """
        Loads the SpanMarkerModel from the specified path.

        Returns:
            SpanMarkerModel: The loaded model.
        """
        try:
            model = SpanMarkerModel.from_pretrained(self.model_path)
            self.logger.info(f"Model loaded successfully from {self.model_path}")
            return model
        except Exception as e:
            self.logger.error(f"Failed to load model from {self.model_path}: {e}")
            raise

    def predict(self, text: str) -> List[Dict[str, Any]]:
        """
        Runs inference on the given text and returns the extracted entities.

        Parameters:
            text (str): The input text for which to predict entities.

        Returns:
            List[Dict[str, Any]]: A list of entities with their respective information.
        """
        try:
            entities = self.model.predict(text)
            self.logger.info(f"Prediction successful for input text: {text[:30]}...")
            return entities
        except Exception as e:
            self.logger.error(
                f"Prediction failed for input text: {text[:30]}... Error: {e}"
            )
            raise

    def format_predictions(self, predictions: List[Dict[str, Any]]) -> str:
        """
        Formats the predictions into a structured string that can be easily read and used.

        Parameters:
            predictions (List[Dict[str, Any]]): The list of entities predicted by the model.

        Returns:
            str: A formatted string of predictions.
        """
        formatted = ""
        for pred in predictions:
            formatted += (
                f"{pred['entity_group']}: {pred['word']} (Score: {pred['score']:.2f})\n"
            )
        return formatted.strip()

    def format_predictions(self, predictions: List[Dict[str, Any]]) -> str:
        formatted = ""
        for pred in predictions:
            formatted += (
                f"{pred['entity_group']}: {pred['word']} (Score: {pred['score']:.2f})\n"
            )
        return formatted.strip()

    def generate_metadata(self, predictions: List[Dict[str, Any]]) -> Dict[str, Any]:
        metadata = {}
        for pred in predictions:
            key = pred["entity_group"]
            if key not in metadata:
                metadata[key] = []
            metadata[key].append(pred["word"])
        return metadata

    def text_chunk(self, text, chunk_size=512):
        """
        Breaks down text into smaller chunks of a specified size.

        Parameters:
            text (str): The text to be chunked.
            chunk_size (int): The maximum size of each text chunk.

        Returns:
            List[str]: A list of text chunks.
        """
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    def analyze_text(self):
        entities = self.predict()
        output_str = f"Entities found in the text: {self.text}\n"
        key_value_pairs = self.format_predictions(entities)
        output_str += "\n".join([f"{kvp['word']}" for kvp in key_value_pairs])
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

    def upload_enriched_text(self, corpus_id, document_id, text, predictions):
        metadata = self.generate_metadata(predictions)
        enriched_text = self.format_predictions(predictions) + "\n\n" + text
        try:
            response, success = self.vectara_client.index_document(
                corpus_id, document_id, "Enriched Text", metadata, enriched_text
            )
            if success:
                self.logger.info("Enriched document uploaded successfully.")
            else:
                self.logger.error("Failed to upload enriched document.")
        except Exception as e:
            self.logger.error(f"An error occurred while uploading the document: {e}")

    def span_enhance(self, corpus_id_1, corpus_id_2, folder_path):
        logging.info("Starting the processing and upload of documents.")  
          
        # Create two corpora, one for raw uploads and one for processed uploads  
        corpus_response_1 = self.create_corpus("Corpus 1", "First corpus for raw uploads")  
        corpus_id_1 = corpus_response_1['data']['corpusId']  
        corpus_response_2 = self.create_corpus("Corpus 2", "Second corpus for processed uploads")  
        corpus_id_2 = corpus_response_2['data']['corpusId']  
          
        upload_results = self.vectara_client.index_documents_from_folder(corpus_id_1, folder_path, return_extracted_document=True)  
        for document_id, success, response in upload_results:  
            logging.debug(f"Received response for document {document_id}: {response}")  
            if not success:  
                logging.warning(f"Upload failed for document {document_id}.")  
                continue  
            if response is None or response == '':  
                logging.warning(f"No response received for document {document_id}.")  
                continue  
    
            # If the response is a string, try to parse it as JSON  
            if isinstance(response, str):  
                try:  
                    response = json.loads(response)  
                except json.JSONDecodeError as e:  
                    logging.warning(f"Failed to parse response as JSON for document {document_id}: {e}")  
                    logging.debug(f"Response content: '{response}'")  
                    continue
            
            # Now we can safely assume response is a dictionary and use the 'get' method  
            document_text_sections = response.get('document', {}).get('section', [])  
            if not document_text_sections:  
                logging.warning(f"Text sections not found or invalid format in the response for document {document_id}.")  
                continue  
              
            # Combine text from all sections  
            document_text = " ".join(section['text'] for section in document_text_sections if 'text' in section)  
              
            chunks = self.text_chunk(document_text)  
            for chunk_index, chunk in enumerate(chunks):  
                # Use the analyzed_text method to process text and extract entities  
                self.text = chunk  
                output_str, entities = self.analyze_text()  # Assuming that analyze_text now returns a tuple  
  
                # Prepend the output_str to the chunk  
                chunk_with_entities = output_str + "\n" + chunk  
  
                # Create metadata with extracted entities  
                metadata_json = json.dumps({"entities": entities})  
                  
                # Index the processed chunk with extracted entities as metadata  
                self.vectara_client.index_text(  
                    corpus_id=corpus_id_2,  
                    document_id=f"{document_id}_chunk_{chunk_index}",  
                    text=chunk_with_entities,  
                    metadata_json=metadata_json  
                )  
          
        logging.info("Finished processing and uploading documents.")  
        return corpus_id_1, corpus_id_2  
    