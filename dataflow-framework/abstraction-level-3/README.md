Level 3: Dynamic Config-Driven Pipeline

## Overview

In this level, the pipeline logic is entirely **decoupled from the code**. The processing steps are defined in a `pipeline.yaml` config file using **dotted import paths**. This makes the system highly extensible — users can plug in their own processors without modifying the source code.

## Project Structure

```
├── README.md
├── __init__.py
├── cli.py
├── core.py
├── custom_types.py
├── main.py
├── pipeline.py
├── pipeline.yaml
├── pipeline_text.txt
├── processors
│   ├── __init__.py
│   ├── snake.py
│   └── upper.py
├── text.txt
```

## Features
- CLI accepts --input, --output, and now --config
- Loads processor functions dynamically from YAML config
- Easily extensible with new custom processors
- Handles import errors gracefully

## How to Run
From the `abstraction-level-3/` directory:
```bash
python main.py --input path/to/input.txt --output path/to/output.txt --config pipeline.yaml # defaults to pipeline.yaml
```