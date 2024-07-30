import json


class Store:
    def __init__(self):
        try:
            self.load()
        except FileNotFoundError:
            self.save({})
    
    def save(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f)

    def load(self):
        with open("data.json", "r") as f:
            return json.load(f)

    def get(self, key):
        data = self.load()
        value = data.get(key, None)
        return value

    def set(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)
