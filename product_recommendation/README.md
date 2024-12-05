# Unsupervised Learning Project - Product Recommendation System

In this project, a product recommendation system will be created on a product purchase data taken from Google Analytics.

With the purchase and user info, system will decide which products will be recommended to a specific user.

## Specification

Product Recommendation System

Application Description:
A simple recommendation system for products based on user purchases and product properties

Data:

Product purchase features: user_id, ga_session_id, country, device, type, item_id, date
Product features: id, name, brand, variant, category, price_in_usd
User features: id, ltv, date

Data source:

Google Analytics purchase, product and user data

Model:

K-Means algorithm: This model can create user / product clusters grouping similar records. 
For better results, product data should be merged to the purchase data. For better result, K-Means can be also applied to the product data additionally to identify the similar products.

### Features

1. Data collection and preprocessing
2. Data merging, feature extraction and encoding
3. Model execution (k-Means)
4. API interface for inputting parameters
5. Product recommendations with already calculated model based on user input (either user, or user / product tuple)

#### Limitations
* Time
* Keep number of genres low

### Requirements

#### Data requirements

1. Product purchase features:
    * User id
    * Session id
    * Country
    * Device
    * Type
    * Product id
    * Date time
2. Product features:
    * Product id
    * Name
    * Brand
    * Variant
    * Category
    * Price
3. User data:
    * User id
    * LTV
    * Subscription time

#### Software requirements

**LIBRARIES**

* pandas: Data manipulation and analysis
* scikit-learn: machine learning algorithms and preprocessing
* numpy: numerical operations
* matplotlib: show dialogs for cluster groupings or other needs
* fastapi: REST API
* uvicorn: REST API

**CLASSES and METHODS**

1. `DataProvider`
    * Responsible for loading, cleaning and preprocessing product & purchase data. And also it merges product and purchase data for detailed clustering. 
    * `get_purchase_data()`
    * `get_product_data()`
    * `get_merged_data()`
    * `get_item_info()`
    * `get_user_transaction_info()`
2. `ProductRecommender`
    * Runs KMeansEngine with the data it gets from DataProvider and processes the input / output
    * `run()`: Gets the initial data and initiates the KMeansEngine 
    * `get_recommendation()`: Processes input, runs KMeans recommendation and processes output
5. `KMeansEngine`
    * Implements the KMeans Algorithm
    * `train()`: Train the recommendation model
    * `get_recommendations()`: Generate recommendations for a user and possibly a product
6. `APIInterface`
    * Manages REST API interfaces
    * `run_api_interface()`: Initiates and configures REST API 
    * `get_recommendations()`: Implements GET API for /recommendations. Takes the user id and the product id, and returns the list of recommended product ids.

## Discussion

Product recommendation system will recommend products to user based on their previous purchases and product similarities like price, category, name and brand.

System tries to use k-Means algorithm to identify product clusters. 

To simulate the behavior of the user is visiting a product detail page, both user id and product id is processed to get the recommendations for that user and for that product.
For this scenario, /recommendations?user_id=X&item_id=Y API service is used.

To simulate the behavior of the user is visiting a main page, only user id is processed to get the recommendations for that user.
For this scenario, /recommendations?user_id=X API service is used.

In the logs, related purchase and product data with the user and the product is shown. Also the recommended items are listed in detail to check whether the algorithm is working good or not.
