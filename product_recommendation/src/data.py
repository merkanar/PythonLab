import pandas as pd


class DataProvider:

    def __init__(self):
        self.purchase_data = None
        self.product_data = None
        self.user_data = None
        self.merged_data = None

    def get_purchase_data(self):
        if self.purchase_data is None:
            self.purchase_data = pd.read_csv('../data/events1.csv')
        return self.purchase_data

    def get_product_data(self):
        if self.product_data is None:
            self.product_data = pd.read_csv('../data/items.csv')
        return self.product_data

    def get_user_data(self):
        if self.user_data is None:
            self.user_data = pd.read_csv('../data/users.csv')
        return self.user_data

    def get_merged_data(self):
        if self.merged_data is None:
            self.merged_data = pd.merge(self.get_purchase_data(), self.get_product_data(), left_on='item_id', right_on='id').drop(
            ['ga_session_id', 'type', 'device', 'variant', 'date', 'id', 'country'], axis=1)
        return self.merged_data

    def get_item_info(self, item_id):
        item_info = self.product_data[(self.product_data['id'] == item_id)]
        if item_info.shape[0] > 0:
             return item_info.iloc[0]
        return None

    def get_user_transaction_info(self, user_id):
        return self.merged_data[(self.merged_data['user_id'] == user_id)]