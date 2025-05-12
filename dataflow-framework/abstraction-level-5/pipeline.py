import yaml
from dag import DAG
from processors.trim import trim
from processors.line_counter import LineCounterProcessor
from processors.tagging import TagError, TagWarn

class ProcessorRegistry:
    """
    A registry for managing processors and their types.
    """
    _registry = {
        "trim": lambda: trim,
        "tag_error": TagError,
        "tag_warn": TagWarn,
        "count": LineCounterProcessor,
    }

    @classmethod
    def get_processor(cls, processor_type: str):
        """
        Retrieves the processor based on its type.
        """
        processor_class = cls._registry.get(processor_type)
        if processor_class is None:
            raise ValueError(f"Unknown processor type: {processor_type}")
        return processor_class()

def load_dag_pipeline(config_path: str) -> DAG:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    dag = DAG()

    # Register nodes
    for node in config.get("nodes", []):
        name = node["name"]
        ptype = node["type"]

        try:
            processor = ProcessorRegistry.get_processor(ptype)
        except ValueError as e:
            print(f"Error loading processor for node '{name}': {e}")
            continue  # Skip this node if processor is invalid

        dag.add_node(name, processor)

    # Register edges
    for edge in config.get("edges", []):
        from_node = edge["from"]
        to_node = edge["to"]
        tag = edge.get("tag")

        # Add the edge to the DAG
        dag.add_edge(from_node, to_node, tag)

    return dag

# Example usage:
# dag = load_dag_pipeline("pipeline.yaml")
# dag.execute(lines)
