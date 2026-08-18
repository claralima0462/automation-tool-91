import json

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'Error: Configuration file {self.filepath} not found.')
            return {}
        except json.JSONDecodeError:
            print(f'Error: Configuration file {self.filepath} contains invalid JSON.')
            return {}
        except Exception as e:
            print(f'Unexpected error occurred: {str(e)}')
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.settings, file, indent=4)
        except Exception as e:
            print(f'Error saving configuration: {str(e)}')
