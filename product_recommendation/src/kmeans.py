import time

from pandas import Series
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


class KMeansEngine:

    def __init__(self):
        self.merged_data = None

    def train(self, merged_data):
        print("Training started..")
        start_time = time.time()

        self.merged_data = merged_data

        # 2. Encode Categorical and Scale Numerical Features
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), ['price_in_usd']),
                ('cat', OneHotEncoder(), ['brand', 'category'])
            ]
        )
        processed_data = preprocessor.fit_transform(self.merged_data)

        # 6. Apply K-means Clustering on Extracted Features
        n_clusters = 100  # Define the number of clusters
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(processed_data)

        # Assign cluster labels to each entry
        self.merged_data['cluster'] = kmeans.labels_
        duration = time.time() - start_time
        print("Training ended in ", duration, " seconds")

    def get_recommendation(self, user_id, item_id):

        filtered_data_by_user_id = self.merged_data[(self.merged_data['user_id'] == user_id)]

        most_frequent_items_from_user: Series = self.find_most_common_items(filtered_data_by_user_id, item_id)

        if item_id is not None:
            filtered_data_by_item_id = self.merged_data[(self.merged_data['user_id'] == user_id) & (self.merged_data['item_id'] == item_id)]
            if filtered_data_by_item_id.shape[0] == 0:
                filtered_data_by_item_id = self.merged_data[(self.merged_data['item_id'] == item_id)]
                if filtered_data_by_item_id is not None:
                    most_frequent_items_from_user = most_frequent_items_from_user._append(self.find_most_common_items(filtered_data_by_item_id, item_id))

        item_ids = []

        for index, value in most_frequent_items_from_user.items():
            item_ids.append(index)

        return item_ids

    def find_most_common_items(self, filtered_data, item_id):
        counts = filtered_data['cluster'].value_counts()
        if counts.empty:
            counts = self.merged_data['cluster'].value_counts()

        most_frequent_cluster = counts.idxmax()
        same_cluster_items = self.merged_data[
            (self.merged_data['cluster'] == most_frequent_cluster) & (self.merged_data['item_id'] != item_id)]
        return same_cluster_items['item_id'].value_counts().nlargest(5)





