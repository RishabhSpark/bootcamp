from setuptools import setup, find_packages

setup(
    name="rishabh-hello",
    version="1.1.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer>=0.6.0",
        "rich>=13.0.0"
    ],
    entry_points={
        'console_scripts': [
            'rishabh-hello=rishabh_hello.cli:app',
        ],
    },
)