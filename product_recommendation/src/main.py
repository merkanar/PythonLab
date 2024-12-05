from api_interface import run_api_interface
from product_recommender import ProductRecommender

# Run the recommender app
if __name__ == '__main__':
    product_recommender = ProductRecommender()
    product_recommender.run()
    print("Product recommender initialized, please use the REST API 'http://localhost:8000/recommendations?user_id=X&item_id=Y'")
    run_api_interface(product_recommender)

