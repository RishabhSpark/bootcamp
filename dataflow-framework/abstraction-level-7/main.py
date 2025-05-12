import threading
import time
from metrics.metrics import Metrics
import argparse
from dashboard import start_dashboard
import importlib
import yaml

metrics = Metrics()

def load_processors(config):
    """
    Dynamically loads processors based on the provided configuration.
    """
    processors = {}
    for node in config["nodes"]:
        tag = node["tag"]
        module_path = node["type"]
        try:
            module_name, class_name = module_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            processor_class = getattr(module, class_name)
            processors[tag] = processor_class()  # Instantiate the class
        except (ImportError, AttributeError) as e:
            print(f"Error loading processor '{tag}' from '{module_path}': {e}")
    return processors

def run_pipeline(processors, input_lines, trace_enabled):
    """
    Runs the pipeline over input lines with optional tracing.
    """
    for line in input_lines:
        queue = [("start", line.strip())]
        trace = []
        
        while queue:
            tag, current_line = queue.pop(0)
            processor = processors.get(tag)
            if not processor:
                print(f"No processor found for tag '{tag}'")
                continue
            
            try:
                start_time = time.time()
                output_lines = processor.process(current_line)
                duration = time.time() - start_time
                
                # Record processing time and errors
                metrics.add_processing_time(tag, duration)
                
                # If tracing is enabled, record the trace
                if trace_enabled:
                    trace.append(tag)
                
                queue.extend(output_lines)
            except Exception as e:
                print(f"[ERROR] {tag}: {e}")
                metrics.increment_errors(tag)
        
        if trace_enabled and trace:
            metrics.add_trace(trace)
            
            
def main(input_file, config_file, trace_enabled):
    with open(input_file) as f:
        input_lines = f.readlines()

    with open(config_file) as f:
        config = yaml.safe_load(f)

    processors = load_processors(config)

    dashboard_thread = threading.Thread(target=start_dashboard)
    dashboard_thread.daemon = True
    dashboard_thread.start()

    run_pipeline(processors, input_lines, trace_enabled)

if __name__ == "__main__":
    main()