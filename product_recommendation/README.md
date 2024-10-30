# Supervised Learning Project - Product Recommender

In this project, a product recommendation system will be created on a product purchase data taken from Google Analytics.

With the purchase and user info, system will decide which products will be recommended to a specific user.

## Specifikation

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

Alternative 1: Use a simple k-Means algorithm. This model can create user / product clusters grouping similar records. 
For better results, product data should be merged to the purchase data.

Alternative 2: Collaborative Filtering

Alternative 3: Use cosine similarities

### Features

1. Data collection and preprocessing
2. Mergimg, feature extraction and encoding
3. Model training (k-NN or Collaborative Filtering)
4. User interface for inputting preferences
5. Book recommendations based on user input

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

**CLASSES and METHODS**

1. `PurchaseData`
    * Responsible for loading, cleaning and preprocessing product purchase data
    * `load_data()`
    * `clean_data()`
    * `preprocess_data()`
2. `ProductData`
    * Handles user information
    * `load_product_data()`
3. `UserData`
    * Handles user information
    * `load_user_data()`
4. `FeatureExtractor`
    * Extracts and encodes features from purchase, product and user data
    * `encode_categorical_features()`: One-hot encode categorical features
    * `normalize_numerical_features()`: Scale numerical features
    * `create_feature_matrix()`: Combine all features into a single matrix
5. `RecommendationModel`
    * Implements the chosen recommendation algorithms (k-NN)
    * `train_model()`: Train the recommendation model
    * `get_recommendations()`: Generate recommendations for a user
6. `UserInterface`
    * Manages user interactions and displays recommendations
    * `get_user_input()`: Prompt user for preferences
    * `display_recommendations()`: Show recommended books to the user

## Discussion

Product recommendation system will recommend products to user based on their previous purchases and product similarities like price, category, name and brand.

System will try to use alternative methods and select recommendations using all of them if possible.
