from typing import List, Dict

class DataProcessor:
    """Class to process data records."""

    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize the processor with data records.

        Args:
            data (List[Dict[str, str]]): List of data records as dictionaries.
        """
        self.data = data

    def filter_data(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filter records based on a specific key-value pair.

        Args:
            key (str): The key to filter by.
            value (str): The value that the key must match.

        Returns:
            List[Dict[str, str]]: Filtered list of records.
        """
        return [record for record in self.data if record.get(key) == value]

    def sort_data(self, key: str) -> List[Dict[str, str]]:
        """Sort records by a specific key.

        Args:
            key (str): The key to sort by.

        Returns:
            List[Dict[str, str]]: Sorted list of records.
        """
        return sorted(self.data, key=lambda record: record.get(key))

    def summarize_data(self, key: str) -> Dict[str, int]:
        """Summarize the counts of unique values in a specific key.

        Args:
            key (str): The key to summarize.

        Returns:
            Dict[str, int]: A dictionary with unique values as keys and their counts as values.
        """
        summary = {}
        for record in self.data:
            value = record.get(key)
            if value:
                summary[value] = summary.get(value, 0) + 1
        return summary
