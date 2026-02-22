"""API routes for prediction and health checks."""

from typing import Dict
import numpy as np
from fastapi import APIRouter, HTTPException

from .schemas import PredictionInput, PredictionOutput
from .config import FEATURE_SETS, SUPPORTED_COHORTS

router = APIRouter()


def setup_routes(models: Dict):
    """Setup all routes with loaded models."""

    @router.get("/", tags=["Info"])
    def read_root():
        """Root endpoint with API information."""
        return {
            "message": "School Lag Prediction API",
            "version": "1.0.0",
            "available_endpoints": {"predict": "/predict", "health": "/health"},
        }

    @router.get("/health", tags=["Info"])
    def health_check():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "models_loaded": list(models.keys()),
            "supported_cohorts": SUPPORTED_COHORTS,
        }

    @router.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
    def predict(data: PredictionInput):
        """
        Make a prediction based on student features and cohort year.

        - **years**: Cohort year (1, 2, or 3)
        - **years=1**: Only current year features (5 features)
        - **years=2**: Current year + 1-year lag features (10 features)
        - **years=3**: Current year + 1 and 2-year lag features (15 features)
        """
        cohort = data.years

        # Validate cohort
        if cohort not in SUPPORTED_COHORTS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid cohort. Must be one of {SUPPORTED_COHORTS}.",
            )

        # Get required features for this cohort
        required_features = FEATURE_SETS[cohort]

        # Build feature vector
        features = []
        for feature in required_features:
            try:
                value = getattr(data, feature)
                if value is None:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Feature '{feature}' is required for cohort {cohort} but was not provided.",
                    )
                features.append(value)
            except AttributeError:
                raise HTTPException(
                    status_code=400,
                    detail=f"Feature '{feature}' is required for cohort {cohort}.",
                )

        # Convert to numpy array for prediction
        X = np.array(features).reshape(1, -1)

        # Get model and make prediction
        model = models[cohort]
        prediction = model.predict(X)[0]
        prediction_proba = model.predict_proba(X)[0]

        # Get probability of having lag (class 1)
        probability = (
            prediction_proba[1] if len(prediction_proba) > 1 else prediction_proba[0]
        )

        return PredictionOutput(
            cohort_year=cohort,
            prediction=int(prediction),
            features_used=required_features,
        )

    @router.get("/features/{cohort}", tags=["Info"])
    def get_cohort_features(cohort: int):
        """Get the list of features required for a specific cohort."""
        if cohort not in SUPPORTED_COHORTS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid cohort. Must be one of {SUPPORTED_COHORTS}.",
            )

        return {
            "cohort": cohort,
            "features": FEATURE_SETS[cohort],
            "feature_count": len(FEATURE_SETS[cohort]),
        }

    return router
