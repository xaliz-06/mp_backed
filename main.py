import json
from src.major_project import Predictor, load_dummy_data

def main():
    predictor = Predictor()
    input_data = load_dummy_data()

    input_txt = input_data["conversation"]
    predicted_class, tokens = predictor.generate_predicted_class_and_tokens(input_txt=input_txt)

    prescription = predictor.generate_prescription(predicted_class=predicted_class, tokens=tokens, input_txt=input_txt) 

    if prescription:
        summary_text = f"This prescription includes medications like {', '.join(prescription.get('Medicines', ['None']))}. Recommended tests are {', '.join(prescription.get('Tests', ['None']))}. Key advice is {', '.join(prescription.get('Advice', ['None']))}. Ensure to follow the dosage and duration carefully and seek follow-up if symptoms persist."
    else:
        summary_text = "No relevant prescription information extracted from the provided text."

    ordered_keys = ["Age", "Sex", "Sign_symptom", "Severity", "Diagnostic_procedure", "Biological_structure", "Medicines", "Dosage"]
    for key in ordered_keys:
        if key in prescription:
            print(f"{key}: {', '.join(prescription[key])}")

    print(json.dumps({"summary": summary_text, "prescription": prescription}, indent=4))

if __name__ == '__main__':
    main()