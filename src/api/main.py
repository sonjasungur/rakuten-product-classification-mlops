import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

MODEL_PATH = "outputs/models/rakuten_text_classifier.joblib"

app = FastAPI(
    title="Rakuten Product Classification API",
    description="Demo API for product category prediction using a trained ML model.",
    version="1.0.0",
)

prediction_counter = Counter(
    "rakuten_predictions_total",
    "Total number of product classification predictions",
)

class ProductInput(BaseModel):
    item_name: str
    item_caption: str

model = joblib.load(MODEL_PATH)

@app.get("/")
def health_check():
    return {"status": "ok", "service": "rakuten-product-classification-api"}

@app.post("/predict")
def predict_product_category(product: ProductInput):
    prediction_counter.inc()

    text = product.item_name + " " + product.item_caption
    prediction = model.predict([text])[0]

    return {
        "item_name": product.item_name,
        "item_caption": product.item_caption,
        "predicted_category": prediction,
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)