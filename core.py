import json
import os
class AutoClickerData:
    def __init__(self, data_file='click_data.json'):
        self.data_file = data_file
        self.click_data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.click_data, file)

    def add_click_event(self, event):
        self.click_data.append(event)
        self.save_data()

    def get_all_clicks(self):
        return self.click_data

    def clear_click_data(self):
        self.click_data = []
        self.save_data()
