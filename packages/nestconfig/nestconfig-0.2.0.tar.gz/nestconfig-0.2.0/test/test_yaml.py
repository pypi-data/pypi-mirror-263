from nestconfig import NestConfig
from dataclasses import dataclass, field
import yaml


@dataclass
class ModelConfig:
    N_LAYER: int = 2


@dataclass
class Config(NestConfig):
    LEARNING_RATE: float = 0.001
    BATCH_SIZE: int = 64
    MODEL: ModelConfig = field(default_factory=ModelConfig)


# Load configuration updates from an external YAML file
with open('config.yaml', 'r') as file:
    config_updates = yaml.safe_load(file)

# Create a Config instance and merge updates
config = Config()
config.merge_updates(config_updates)

print(config.MODEL.N_LAYER)  # 6

# Or you can directly load YAML file with merge_yaml
config = Config()
config.merge_yaml('config.yaml')
print(config.MODEL.N_LAYER)  # 6
