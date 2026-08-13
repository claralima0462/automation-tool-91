from typing import Dict, Any

class Config:
    """Configuration manager for the autoclicker tool."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        """Initialize the configuration with provided settings.

        Args:
            settings (Dict[str, Any]): A dictionary containing configuration settings.
        """
        self.settings = settings

    def get_setting(self, key: str) -> Any:
        """Retrieve a setting value by key.

        Args:
            key (str): The key of the setting to retrieve.

        Returns:
            Any: The value associated with the provided key, or None if not found.
        """
        return self.settings.get(key)

    def set_setting(self, key: str, value: Any) -> None:
        """Set a value for a specific setting key.

        Args:
            key (str): The key for the setting to set.
            value (Any): The value to assign to the setting key.
        """
        self.settings[key] = value

    def load_from_file(self, file_path: str) -> None:
        """Load settings from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing settings.
        """
        import json
        with open(file_path, 'r') as f:
            self.settings = json.load(f)

    def save_to_file(self, file_path: str) -> None:
        """Save current settings to a JSON file.

        Args:
            file_path (str): Path to the JSON file where settings will be saved.
        """
        import json
        with open(file_path, 'w') as f:
            json.dump(self.settings, f, indent=4)
