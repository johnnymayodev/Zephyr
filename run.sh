#! /bin/bash

# CHECK FOR DEBUG MODE

if [ "$1" = "--debug" ]; then
    echo "Running in debug mode"
    CLA="--debug"
else
    CLA=""
fi

# CHECK CWD

DIR=$(pwd | grep -o '[^/]*$')

if [ $DIR != "Zephyr" ]; then
    echo "Please run the script from the Zephyr directory"
    exit 1
fi

# CHECK FOR PYTHON

HAS_PYTHON=false
PYTHON3=false

if [ -x "$(command -v python3)" ]; then
    HAS_PYTHON=true
    PYTHON3=true
elif [ -x "$(command -v python)" ]; then
    HAS_PYTHON=true
fi

if [ $HAS_PYTHON = false ]; then
    echo "Python is not installed"
    exit 1
fi

# RUN APP

if [ $PYTHON3 = true ]; then
    python3 zephyr/server.py $CLA
else
    python zephyr/server.py $CLA
fi