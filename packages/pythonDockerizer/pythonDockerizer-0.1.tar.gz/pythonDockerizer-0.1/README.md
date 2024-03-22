# create_docker_file

## Overview
`pythonDockerizer` is a Python script for generating a Dockerfile based on specified parameters.

## Usage
```bash
python pythonDockerizer/dockerize.py [options]
```
## Example
```bash
python pythonDockerizer/dockerize.py --entrypoint app --version 3.9 --filename Dockerfile --port 8080
```