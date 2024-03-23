# rmk2

## Overview

This package serves as a personal toolbox, gathering various functions that I keep
reaching for when working on various projects.

## Installation

This project is written in `python3`.

It uses `pipenv` for dependency management, `pytest` for testing, and `black` for formatting.

### Python environment

To retrieve the full source code and initialise a local virtual environment including
required packages, run:

```
# Git
git clone https://gitlab.com/rmk2/rmk2-py.git

# Pipenv
# NB: with the switch -d, pipenv also installs development packages, such as pytest
pipenv install -d

# Activate environment
pipenv shell

# Optional: (re)generate a test-requirements.txt via pipenv
pipenv requirements --dev > test-requirements.txt

# Optional: Install locally checked out package
pip install -e .
```
