"""Routes package initialization."""

from .routes import setup_routes
from .schemas import PredictionInput, PredictionOutput
from .config import FEATURE_SETS, SUPPORTED_COHORTS

__all__ = [
    "setup_routes",
    "PredictionInput",
    "PredictionOutput",
    "FEATURE_SETS",
    "SUPPORTED_COHORTS",
]
