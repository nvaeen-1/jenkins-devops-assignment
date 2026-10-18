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

## Feature: Calculator Usage

The calculator supports addition, subtraction,
multiplication, and division.

Run the application with:
python3 src/calculator.py

Run automated tests with:
python3 -m unittest discover -s tests -v
