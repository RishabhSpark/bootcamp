# rishabh-hello

`rishabh-hello` is a lightweight Python command-line tool that prints a friendly greeting using the power of [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).

It greets a person by name if provided, or defaults to "World".

Asciinema Link: https://asciinema.org/a/SQRsxnGGOPktKAqJD0SFsCkUz

--
## Features

- Clean and modern CLI powered by **Typer**
- Stylish terminal output with **Rich**
- Default greeting: `Hello, World!`

--

## Installation

To install the package from [TestPyPI](https://test.pypi.org/):

```bash
pip install -i https://test.pypi.org/simple/ rishabh-hello
```

--

## Usage
After installing, simply run the following command in your terminal:

1. With a name:
```bash
rishabh-hello --name Rishabh
```

Output
```bash
Hello, Rishabh!
```

2. Without a name:
```bash
rishabh-hello
```

Output
```bash
Hello, World!
```