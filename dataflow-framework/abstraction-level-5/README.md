# DAG Routing and Conditional Flows

## Overview
In this level, we introduce a Directed Acyclic Graph (DAG) based pipeline, which allows for conditional routing of lines. Each line can take a different path through the system based on its content, tags, or conditions. This enables flexible and dynamic workflows, making it possible to process data differently depending on its type.

## Project Structure
```
├── __init__.py
├── cli.py
├── custom_types.py
├── dag.py
├── dag_pipeline.yaml
├── main.py
├── pipeline.py
├── processors
│   ├── __init__.py
│   ├── length_filter.py
│   ├── line_counter.py
│   ├── tagging.py
│   └── trim.py
└── text.txt
```

## Features
- DAG-based routing with tag-based conditional processing.
- Extensible: Add new processors and routes in the YAML file.
- Fan-out/Fan-in: Support for routing to multiple processors and aggregating inputs.

## How to Run
From the abstraction-level-5/ directory:
```bash
python main.py --input path/to/input.txt --config dag_pipeline.yaml --output path/to/output.txt
```