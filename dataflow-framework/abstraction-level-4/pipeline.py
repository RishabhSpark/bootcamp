import yaml
import importlib
import sys
import os
from typing import Iterator, List
from inspect import signature, isclass

from custom_types import StreamProcessor
from core import wrap_line_processor

def load_pipeline_from_config(config_path: str) -> List[StreamProcessor]:
    """Load and instantiate stream processors from a YAML config file."""
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    pipeline_steps = config.get('pipeline', [])
    processors: List[StreamProcessor] = []

    for step in pipeline_steps:
        processor_path = step.get('type')
        config_args = step.get('config', {})

        if processor_path:
            module_name, name = processor_path.rsplit('.', 1)
            try:
                module = importlib.import_module(module_name)
                target = getattr(module, name)

                if isclass(target):
                    # If it's a class, initialize with config
                    instance = target(**config_args)
                    processors.append(instance)
                else:
                    # It's a function, check if it needs wrapping
                    sig = signature(target)
                    if len(sig.parameters) == 1 and sig.return_annotation is str:
                        target = wrap_line_processor(target)
                    processors.append(target)

            except Exception as e:
                raise ValueError(f"Error loading processor {processor_path}: {e}")

    return processors


def run_pipeline(lines: Iterator[str], processors: List[StreamProcessor]) -> Iterator[str]:
    for processor in processors:
        lines = processor(lines)
    return lines