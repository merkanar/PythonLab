from itertools import product

from product_recommender import ProductRecommender
from fastapi import FastAPI
import uvicorn

app = FastAPI()
product_recommender = ProductRecommender()


@app.get("/get-recommendation")
async def get_recommendation(user_id: int = None, item_id: int = None):
    if user_id is None:
        return "Please provide user id, usage: '/get_recommendation?user_id=X&item_id=Y'"
    return product_recommender.get_recommendation(user_id, item_id)

# Run the recommender app
if __name__ == '__main__':
    product_recommender.run()
    print("Product recommender initialized, please use the REST API 'http://localhost:8000/get_recommendation?user_id=X&item_id=Y'")
    uvicorn.run(app, host='localhost', port=8000)