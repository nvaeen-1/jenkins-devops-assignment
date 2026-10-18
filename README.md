# DevOps CI Project

A simple Python application demonstrating Git, GitHub,
branching, pull requests, Jenkins and continuous integration.

## Requirements
- Python 3
- Git

## Run the application
python3 src/app.py

## Run tests
python3 -m unittest discover -s tests -v

## CI Pipeline
The Jenkins pipeline checks out the source, builds the project,
runs unit tests and reports the final result.
