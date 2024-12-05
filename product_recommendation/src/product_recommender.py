from data import DataProvider
from kmeans import KMeansEngine


def print_item(item):
    print(item['name'], " ", item['brand'], " ", item['category'], " ", item['price_in_usd'])


class ProductRecommender:
    def __init__(self):
        self.data_provider = DataProvider()
        self.kmeans_engine = KMeansEngine()

    #   run the recommender engine
    def run(self):
        self.kmeans_engine.train(self.data_provider.get_merged_data())


    def get_recommendation(self, user_id, item_id):

        print("********** Get Recommendation, ", user_id, " , " , item_id, "*************")

        if item_id is not None:
            item = self.data_provider.get_item_info(item_id)
            if item is not None:
                print('Selected product:')
                print_item(item)
            else:
                item_id = None


        user_transaction_info = self.data_provider.get_user_transaction_info(user_id)

        print('\n\nUser transaction info:')
        for index, item in user_transaction_info.iterrows():
            print_item(item)

        recommendation_list = self.kmeans_engine.get_recommendation(user_id, item_id)


        print('\n\nRecommendations:')
        for item_id in recommendation_list:
            item = self.data_provider.get_item_info(item_id)
            print_item(item)

        print("***********************")

        return recommendation_list





