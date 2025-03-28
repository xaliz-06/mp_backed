from .model_loader import load_model_and_tokenizer

import torch
import re

class Predictor:
    def __init__(self):
        self.model, self.tokenizer = load_model_and_tokenizer()

    def generate_predicted_class_and_tokens(self, input_txt):
        inputs = self.tokenizer(input_txt, return_tensors="pt", truncation=True, padding=True)

        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=2).squeeze().tolist()
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze().tolist())
        return predicted_class, tokens
    
    def generate_prescription(self, predicted_class, tokens, input_txt):
        labels = [self.model.config.id2label[idx] for idx in predicted_class]

        prescription = {
            "Medicines": [],
            "Dosage": [],
            "Frequency": [],
            "Duration": [],
            "Advice": [],
            "Tests": [],
            "Follow-up": [],
            "Diseases": [],
            "Age": [],
            "Sex": [],
            "Severity": [],
            "Sign_symptom": [],
            "Diagnostic_procedure": [],
            "Biological_structure": []
        }

        # Collect entities based on predicted labels
        current_entity = []
        current_label = None

        for token, label in zip(tokens, labels):
            if label != "O":
                entity_type = label.split('-')[-1]
                if entity_type not in prescription:
                    prescription[entity_type] = []  # Handle unexpected entity types
                if label.startswith("B-"):
                    if current_entity and current_label:
                        prescription[current_label].append(" ".join(current_entity).replace(' ##', ''))
                    current_entity = [token]
                    current_label = entity_type
                elif label.startswith("I-") and current_label == entity_type:
                    current_entity.append(token)
            else:
                if current_entity and current_label:
                    prescription[current_label].append(" ".join(current_entity).replace(' ##', ''))
                    current_entity = []
                    current_label = None

        # Final entity append
        if current_entity and current_label:
            prescription[current_label].append(" ".join(current_entity).replace(' ##', ''))

        # Filter out empty fields
        prescription = {k: list(set(v)) for k, v in prescription.items() if v}  # Remove duplicates

        # Remove hyphen between age
        prescription["Age"] = [age.replace("-", "") for age in prescription.get("Age", [])]

        # Fix Diagnostic_procedure output
        prescription["Diagnostic_procedure"] = [proc.replace("##", "") for proc in prescription.get("Diagnostic_procedure", [])]

        ## Ensure medicines are captured correctly
        if "Medicines" not in prescription:
            prescription["Medicines"] = []
        medicine_pattern = re.compile(r"\b(?:paracetamol|ibuprofen|aspirin|antibiotic|antiviral|antifungal|Aceclofenac)\b", re.IGNORECASE)
        medicines_found = medicine_pattern.findall(input_txt)
        prescription["Medicines"].extend(medicines_found)
        return prescription


