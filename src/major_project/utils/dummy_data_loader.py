import json
from pathlib import Path

def load_dummy_data():
    """
    Load dummy data from the JSON file
    """
    data_path = Path(__file__).parent.parent.parent.parent / "data" / "dummy_data.json"
    with open(data_path, "r") as f:
        dummy_data = json.load(f)
    return dummy_data