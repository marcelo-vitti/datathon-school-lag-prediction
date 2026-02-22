import os
import joblib


def save_model(model, cohort, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"model_year{cohort}.pkl")
    joblib.dump(model, path)
    print(f"Model saved at {path}")
