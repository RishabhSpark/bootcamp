# Level 4: Stream Processing and State

## Overview

In this level, we move from simple `str -> str` functions to full **stream-based processing**. This allows for much more powerful behaviors such as:

- **Fan-out**: Returning multiple lines from a single line
- **Fan-in**: Combining multiple lines into one
- **Stateful Processing**: Keeping track of information across multiple lines (e.g., counters, buffers, aggregators)

We also introduce **stateful processors** and allow for **stream-based pipelines** that operate on iterators instead of simple strings.

## Project Structure

```
├── __init__.py
├── cli.py
├── core.py
├── custom_types.py
├── main.py
├── pipeline.py
├── pipeline.yaml
├── processors
│   ├── __init__.py
│   ├── length_filter.py
│   ├── line_counter.py
│   ├── snake.py
│   └── upper.py
└── text.txt
```

## Features
- `Stream Processing:` Each processor now operates on a stream of lines (`Iterator[str] -> Iterator[str]`)
- `Stateful Processors:` Track internal states, such as line counts
- `Flexible Configuration:` Still using YAML-based configuration, but with support for stateful and stream-based processors
- `Fan-out & Fan-in:` Support for emitting multiple lines or combining multiple lines into one

## How to Run
From the abstraction-level-4/ directory:
```bash
python main.py --input path/to/input.txt --config pipeline.yaml --output path/to/output.txt
```