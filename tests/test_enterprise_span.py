import pytest
from unittest.mock import patch, Mock
from vectara_cli.rebel_span.commercial.enterprise import EnterpriseSpan
from vectara_cli.core import VectaraClient
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.data.corpus_data import CorpusData


from unittest.mock import patch

class TestAdvancedQuery:
    pass

@pytest.fixture
def enterprise_span() -> EnterpriseSpan:
    # vectara_client = Mock(VectaraClient)
    config_manager = ConfigManager()
    api_key, customer_id = config_manager.get_api_keys() 
    vectara_client = VectaraClient(api_key=api_key,customer_id=customer_id)
    return EnterpriseSpan(vectara_client, "keyphrase")

def test_get_model_path(enterprise_span):
    assert enterprise_span._get_model_path() == "tomaarsen/span-marker-bert-base-uncased-keyphrase-inspec"

def test_load_model(enterprise_span):
    with patch("span_marker.SpanMarkerModel.from_pretrained") as mock_from_pretrained:
        enterprise_span._load_model()
        mock_from_pretrained.assert_called_with("tomaarsen/span-marker-bert-base-uncased-keyphrase-inspec")

def test_predict(enterprise_span):
    with patch.object(enterprise_span.model, "predict") as mock_predict:
        mock_predict.return_value = [{"entity_group": "Keyphrase", "word": "machine learning", "score": 0.8}]
        predictions = enterprise_span.predict("This is a sample text about machine learning.")
        assert all(isinstance(elem, dict) for elem in predictions)
        assert len(predictions) == 1
        assert predictions[0]["word"] == "machine learning"

def test_format_predictions(enterprise_span):
    predictions = [
        {"entity_group": "Keyphrase", "word": "machine learning", "score": 0.8},
        {"entity_group": "Keyphrase", "word": "deep learning", "score": 0.7}
    ]
    formatted = enterprise_span.format_predictions(predictions)
    assert formatted == "Keyphrase: machine learning (Score: 0.80)\nKeyphrase: deep learning (Score: 0.70)"

def test_generate_metadata(enterprise_span):
    predictions = [
        {"entity_group": "Keyphrase", "word": "machine learning", "score": 0.8},
        {"entity_group": "Keyphrase", "word": "deep learning", "score": 0.7},
        {"entity_group": "Location", "word": "New York", "score": 0.9}
    ]
    metadata = enterprise_span.generate_metadata(predictions)
    assert metadata == {
        "Keyphrase": ["machine learning", "deep learning"],
        "Location": ["New York"]
    }

def test_text_chunk(enterprise_span):
    text = "This is a sample text that needs to be chunked into smaller pieces."
    chunks = enterprise_span.text_chunk(text, chunk_size=20)
    assert len(chunks) == 3
    assert chunks[0] == "This is a sample text"
    assert chunks[1] == " that needs to be "
    assert chunks[2] == "chunked into smaller pieces."

def test_create_corpus(enterprise_span):
    with patch.object(enterprise_span.vectara_client, "create_corpus") as mock_create_corpus:
        mock_create_corpus.return_value = {"data": {"corpusId": "123456"}}
        response = enterprise_span.create_corpus("Test Corpus", "This is a test corpus")
        assert response["data"]["corpusId"] == "123456"

def test_upload_enriched_text(enterprise_span):
    
    vectara_client = enterprise_span
    
    vectara_client.upload_enriched_text(
        1,
        "vectara_employee_handbook-4524365135dc70a59977373c37601ad1.pdf",
        "Hello my name is John."
    )
    
    with patch.object(enterprise_span.vectara_client, "index_document") as mock_index_document:
        mock_index_document.return_value = ({"message": "Document indexed successfully"}, True)
        predictions = [
            {"entity_group": "Keyphrase", "word": "machine learning", "score": 0.8},
            {"entity_group": "Keyphrase", "word": "deep learning", "score": 0.7}
        ]
        enterprise_span.upload_enriched_text("123456", "doc_id_1", "This is a sample text.", predictions)
        mock_index_document.assert_called_with(
            "123456", "doc_id_1", "Enriched Text",
            {"Keyphrase": ["machine learning", "deep learning"]},
            "Keyphrase: machine learning (Score: 0.80)\nKeyphrase: deep learning (Score: 0.70)\n\nThis is a sample text."
        )