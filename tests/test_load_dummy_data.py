from src.major_project.utils.dummy_data_loader import load_dummy_data
import json

def test_load_dummy_data():
    dummy_data = load_dummy_data();

    assert isinstance(dummy_data, dict), "Dummy data should be a dictionary"
    assert "conversation" in dummy_data, "Dummy data must have a 'conversation' key"
    assert isinstance(dummy_data["conversation"], str), "Dummy data must be a string"

    print("Loaded Dummy Data:")
    print(json.dumps(dummy_data, indent=4))

