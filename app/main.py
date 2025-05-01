from fastapi import FastAPI, UploadFile, File, Form
from app.vision_model import find_similar_products
from app.recommender import get_recommendations
from app.sentiment_model import get_sentiment_tags
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to RetailGPT API"}

@app.post("/upload-image/")
def upload_image(file: UploadFile = File(...)):
    similar_products = find_similar_products(file)
    return {"matches": similar_products}

@app.post("/recommend/")
def recommend(user_id: str = Form(...)):
    recs = get_recommendations(user_id)
    return {"recommendations": recs}

@app.post("/review-tags/")
def review_tags(product_id: str = Form(...)):
    tags = get_sentiment_tags(product_id)
    return {"tags": tags}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)