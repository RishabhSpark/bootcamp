import yaml
import importlib
from custom_types import ProcessorFn
from typing import List
import sys
import os

def load_pipeline_from_config(config_path: str) -> List[ProcessorFn]:
    """Load the pipeline steps from a YAML config file."""
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    pipeline_steps = config.get('pipeline', [])
    
    processors = []
    for step in pipeline_steps:
        processor_path = step.get('type')
        if processor_path:
            module_name, func_name = processor_path.rsplit('.', 1)
            try:
                module = importlib.import_module(module_name)
                func = getattr(module, func_name)
                processors.append(func)
            except (ImportError, AttributeError) as e:
                print(f"Error loading function {processor_path}: {e}")
                raise ValueError(f"Error loading processor {processor_path}.")
    
    return processors