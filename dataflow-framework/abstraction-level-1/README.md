# Level 1: Parameters and CLI Interface

## process.py

This script:

- Uses `typer` to define a clean command-line interface
- Accepts input via `--input or -i`, and optionally `--output or -i` and `--mode or -m`
- Loads default values from a `.env` file using `python-dotenv`
- `uppercase` is the default value for `mode`
- Supports multiple processing modes:
  - `uppercase`: Convert each line to uppercase
  - `snakecase`: Replace spaces with underscores and convert to lowercase
- Outputs to `stdout` by default, or to a file if `--output` is provided

## Constraints
- Use only built-in string operations
- Logic is broken into small functions
- All code remains in a single file

---


## Run the script
```bash
python process.py --input path/to/input.txt --ouptut path/to/output.txt --mode snakecase
```