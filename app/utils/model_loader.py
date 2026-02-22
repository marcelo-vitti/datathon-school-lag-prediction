"""Model loading utilities."""

import pickle
import joblib
from pathlib import Path
from typing import Dict


def load_models() -> Dict:
    """Load all trained models from disk."""
    MODELS_DIR = Path(__file__).parent.parent.parent / "training" / "models"

    models = {}
    for cohort in [1, 2, 3]:
        model_path = MODELS_DIR / f"model_yearcohort_{cohort}.pkl"
        try:
            # Try loading with joblib first (more robust for sklearn models)
            models[cohort] = joblib.load(model_path)
            print(f"✓ Loaded model for cohort {cohort} using joblib")
        except Exception as e:
            try:
                # Fallback to pickle with unsafe loading
                with open(model_path, "rb") as f:
                    models[cohort] = pickle.load(f, encoding="latin1")
                print(f"✓ Loaded model for cohort {cohort} using pickle")
            except Exception as pickle_error:
                raise RuntimeError(
                    f"Failed to load model for cohort {cohort}. "
                    f"Joblib error: {e}. Pickle error: {pickle_error}"
                )

    return models
