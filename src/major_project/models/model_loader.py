from transformers import AutoTokenizer, AutoModelForTokenClassification

def load_model_and_tokenizer():
    """
    Load the model and the tokenizer
    """

    model_name = "d4data/biomedical-ner-all"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    return model, tokenizer