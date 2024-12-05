import uvicorn
from fastapi import FastAPI

from product_recommender import ProductRecommender

app = FastAPI()
product_recommender: ProductRecommender

def run_api_interface(_product_recommender: ProductRecommender):
    global product_recommender
    product_recommender = _product_recommender
    uvicorn.run(app, host='localhost', port=8000)


@app.get("/recommendations")
async def get_recommendations(user_id: int = None, item_id: int = None):
    if user_id is None:
        return "Please provide user id, usage: '/recommendations?user_id=X&item_id=Y'"
    return product_recommender.get_recommendation(user_id, item_id)
