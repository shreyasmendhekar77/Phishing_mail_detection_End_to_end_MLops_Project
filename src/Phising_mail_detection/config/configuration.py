from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen='True')
class Data_preprocessing_config:
    root_dir: Path
    unzip_data_dir: Path
    vector_embed_model: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir :Path
    training_data_path: Path
    trained_model_dir: Path