import json
from typing import Any, Dict, List

class AutoClickerDataProcessor:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def filter_data(self, condition: Dict[str, Any]) -> List[Dict[str, Any]]:
        filtered_data = [item for item in self.data if all(item.get(k) == v for k, v in condition.items())]
        return filtered_data

    def serialize_data(self) -> str:
        return json.dumps(self.data, indent=4)

    def deserialize_data(self, json_string: str) -> None:
        self.data = json.loads(json_string)

    def get_summary(self) -> Dict[str, int]:
        summary = {"total_clicks": len(self.data)}
        return summary

# Example usage:
if __name__ == '__main__':
    sample_data = [
        {"timestamp": 1638847000, "x": 100, "y": 200},
        {"timestamp": 1638847010, "x": 150, "y": 250},
    ]
    processor = AutoClickerDataProcessor(sample_data)
    filtered = processor.filter_data({"x": 100})
    summary = processor.get_summary()
    print(filtered)
    print(summary)
    json_output = processor.serialize_data()
    print(json_output)