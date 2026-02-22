"""Pydantic schemas for request/response validation."""

from typing import List
from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    """Input data for prediction with current year features."""

    years: int = Field(..., description="Cohort year (1, 2, or 3)", ge=1, le=3)
    IAA: float = Field(..., description="Current year IAA score")
    IEG: float = Field(..., description="Current year IEG score")
    IPS: float = Field(..., description="Current year IPS score")
    math: float = Field(..., description="Current year Math score")
    portuguese: float = Field(..., description="Current year Portuguese score")

    # Optional lagged features for cohort 2 and 3
    IAA__minus_1: float = Field(None, description="1-year lag IAA score")
    IEG__minus_1: float = Field(None, description="1-year lag IEG score")
    IPS__minus_1: float = Field(None, description="1-year lag IPS score")
    math__minus_1: float = Field(None, description="1-year lag Math score")
    portuguese__minus_1: float = Field(None, description="1-year lag Portuguese score")

    # Optional lagged features for cohort 3
    IAA__minus_2: float = Field(None, description="2-year lag IAA score")
    IEG__minus_2: float = Field(None, description="2-year lag IEG score")
    IPS__minus_2: float = Field(None, description="2-year lag IPS score")
    math__minus_2: float = Field(None, description="2-year lag Math score")
    portuguese__minus_2: float = Field(None, description="2-year lag Portuguese score")


class PredictionOutput(BaseModel):
    """Output data from prediction."""

    cohort_year: int
    prediction: int = Field(
        ..., description="Prediction: 1 if student has lag, 0 otherwise"
    )
    features_used: List[str] = Field(..., description="Features used for prediction")
