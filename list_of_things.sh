#!/bin/sh

# Find python3
PYTHON_TYPE=$(which python3)

[ -z "$PYTHON_TYPE" ] && { echo "Error: Python3 is not installed. Please install to use this script"; exit 1; }

printf '\e[8;50;150t'

chmod +x main.py
$PYTHON_TYPE main.py 


