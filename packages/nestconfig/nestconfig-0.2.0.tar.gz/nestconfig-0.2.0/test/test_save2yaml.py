from nestconfig import NestConfig
from dataclasses import dataclass, field
import argparse


@dataclass
class ModelConfig:
    N_LAYER: int = 2


@dataclass
class Config(NestConfig):
    LEARNING_RATE: float = 0.001
    BATCH_SIZE: int = 64
    MODEL: ModelConfig = field(default_factory=ModelConfig)


# Set up argparse
parser = argparse.ArgumentParser(description='Test merge_opts function.')
parser.add_argument(
        "--opts",
        help="See the Config definition for all options",
        default=["MODEL.N_LAYER", "12"],
        nargs=argparse.REMAINDER,
    )

args = parser.parse_args()

# Create a Config instance and merge command-line options
config = Config()
config.merge_opts(args.opts)

# Save the current Config as yaml file to inspect later on
config.to_yaml("config_new.yaml")
