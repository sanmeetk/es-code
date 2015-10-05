#!/bin/bash -e

if [ ! -d "./venv" ]; then
    virtualenv -q ./venv --no-site-packages
    echo "Virtualenv created."
fi

if [ ! -f "./venv/updated" -o ./requirements.txt -nt ./venv/updated ]; then
    ./venv/bin/pip install -r requirements.txt
    touch ./venv/updated
    echo "Requirements installed."
fi
