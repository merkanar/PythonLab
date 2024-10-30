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

Alternative 1: K-Means algorithm: This model can create user / product clusters grouping similar records. 
For better results, product data should be merged to the purchase data. For better result, K-Means can be also applied to the product data additionally to identify the similar products.

Alternative 2: Collaborative Filtering: This model tries to extract the recommendations from the past purchase data of similar users.

Alternative 3: Cosine similarities:  This approach applies simple correlation for user & product matrix and try to get the close records.  

### Features

1. Data collection and preprocessing
2. Data merging, feature extraction and encoding
3. Model execution (k-Means, Collaborative Filtering, Cosine similarities)
4. User interface for inputting preferences
5. Product recommendations with already calculated models (more than one model can be used) based on user input (either user, or product or user / product tuple)

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
    * `get_user_input()`: Prompt user for preferences (either product id, or user id or product id and user id tuple)
    * `display_recommendations()`: Show recommended products to the user

## Discussion

Product recommendation system will recommend products to user based on their previous purchases and product similarities like price, category, name and brand.

System will try to use alternative methods and select recommendations using all of them if possible.
