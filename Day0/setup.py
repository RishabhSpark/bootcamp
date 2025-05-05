from setuptools import setup, find_packages

setup(
    name="rishabh-hello",
    version="1.1.4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "rich",
        "typer[all]"
    ],
    entry_points={
        'console_scripts': [
            'rishabh-hello=rishabh_hello.cli:app',
        ],
    },
)