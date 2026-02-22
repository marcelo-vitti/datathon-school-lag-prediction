"""Main FastAPI application entry point."""

from fastapi import FastAPI
from routes import setup_routes
from utils.model_loader import load_models

# Create FastAPI app
app = FastAPI(
    title="School Lag Prediction API",
    description="API to predict student lag based on their academic features",
    version="1.0.0",
)

# Load models
models = load_models()

# Setup routes
router = setup_routes(models)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
