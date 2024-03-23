from dataclasses import is_dataclass, asdict
import yaml
from typing import Any, Dict, TypeVar, get_type_hints, List

T = TypeVar('T')


class NestConfig:
    def merge_updates(self, updates: Dict[str, Any]) -> None:
        """Recursively merges updates into the configuration."""
        for key, value in updates.items():
            if hasattr(self, key):
                field_value = getattr(self, key)
                if is_dataclass(field_value):
                    # If the field is a dataclass, recursively merge it
                    if isinstance(value, dict):
                        self._merge_dataclass(field_value, value)
                    else:
                        raise ValueError(
                            f"Expected dict for updating dataclass field "
                            f"'{key}', got {type(value)}")
                else:
                    # Convert and set the value directly
                    setattr(self, key, self._convert_type(key, value, type(self)))
            else:
                raise AttributeError(
                    f"'{type(self).__name__}' object has no attribute '{key}'")

    def merge_yaml(self, yaml_file: str) -> None:
        with open(yaml_file, 'r') as file:
            updates = yaml.safe_load(file)
        self.merge_updates(updates)

    def merge_opts(self, opts: List[str]) -> None:
        assert len(opts) % 2 == 0, "opts list must contain an even number of elements."
        updates = self._parse_cmd_opts(opts)
        self.merge_updates(updates)

    def _parse_cmd_opts(self, opts: List[str]) -> Dict[str, Any]:
        updates = {}
        for i in range(0, len(opts), 2):
            key, value = opts[i], opts[i + 1]
            if '.' in key:
                current_level = updates
                parts = key.split('.')
                for part in parts[:-1]:
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
                current_level[parts[-1]] = self._convert_value(value)
            else:
                updates[key] = self._convert_value(value)
        return updates

    def _convert_value(self, value: str) -> Any:
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            if value.lower() in ['true', 'false']:
                return value.lower() == 'true'
        return value

    def _merge_dataclass(self, instance: Any, updates: Dict[str, Any]) -> None:
        """Helper method for recursively merging updates into a dataclass instance."""
        assert is_dataclass(instance), "Instance must be a dataclass"
        instance_type = type(instance)
        for key, value in updates.items():
            if hasattr(instance, key):
                field_value = getattr(instance, key)
                if is_dataclass(field_value):
                    if isinstance(value, dict):
                        self._merge_dataclass(field_value, value)
                    else:
                        raise ValueError(
                            f"Expected dict for updating nested dataclass field "
                            f"'{key}', got {type(value)}")
                else:
                    setattr(instance, key, self._convert_type(key, value, instance_type))
            else:
                raise AttributeError(
                    f"'{instance_type.__name__}' object has no attribute '{key}'")

    def _convert_type(self, field_name: str, value: Any, dataclass_type: type) -> Any:
        """Converts the value to the correct type based on the field's type hint."""
        hints = get_type_hints(dataclass_type)
        if field_name in hints:
            required_type = hints[field_name]
            if is_dataclass(required_type) and isinstance(value, dict):
                # Create a new instance of the nested dataclass
                return required_type(**value)
            # Additional type conversion logic can be added here
        return value

    @classmethod
    def from_dict(cls: T, config_dict: Dict[str, Any]) -> T:
        """Creates a configuration instance from a dictionary."""
        return cls(**config_dict)

    def to_yaml(self, file_path) -> None:
        """
        Serialize the dataclass to YAML and write it to a file.
        """
        config_dict = self.to_dict(self)
        with open(file_path, 'w') as file:
            yaml.dump(config_dict, file)

    @staticmethod
    def to_dict(instance):
        """
        Convert the dataclass instance to a dictionary, handling nested dataclasses.
        """
        if is_dataclass(instance):
            return {k: NestConfig.to_dict(v) for k, v in
                    asdict(instance).items()}
        else:
            return instance
