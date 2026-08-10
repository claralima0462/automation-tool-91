import json

class DataHandler:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        """Convert data to JSON format."""
        try:
            json_data = json.dumps(self.data)
            return json_data
        except (TypeError, OverflowError) as e:
            return f"Error converting to JSON: {str(e)}"

    def from_json(self, json_string):
        """Parse JSON string to dictionary."""
        try:
            parsed_data = json.loads(json_string)
            return parsed_data
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {str(e)}"

    def filter_data(self, condition):
        """Filter data based on a condition function."""
        if not callable(condition):
            return "Condition must be a callable function"
        return [item for item in self.data if condition(item)]

# Example usage:
# handler = DataHandler([{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}])  
# json_string = handler.to_json()  
# print(handler.from_json(json_string))  
# filtered = handler.filter_data(lambda x: x['name'].startswith('A'))  
# print(filtered)