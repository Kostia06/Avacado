import json


class Store:
    def __init__(self):
        pass

    def save(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f)

    def load(self):
        with open("data.json", "r") as f:
            return json.load(f)

    def get(self, key):
        data = self.load()
        return data[key]
