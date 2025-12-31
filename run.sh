#!/bin/bash

cd "$(dirname "$0")"

if ! command -v python3 &> /dev/null; then
    echo "[-] Error: Python 3 could not be found."
    exit 1
fi

export PYTHONPATH=$PYTHONPATH:$(pwd)

TARGET=$1
ARGS=${@:2}

if [ -z "$TARGET" ]; then
    echo "Usage: ./run.sh <target> [args]"
    echo "Example: ./run.sh 127.0.0.1"
    echo "Example: ./run.sh example.com --ports 80,443"
    exit 1
fi

python3 main.py "$TARGET" $ARGS
