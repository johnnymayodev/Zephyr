#! /bin/bash

if [ "$1" = "--debug" ]; then
    echo "Running in debug mode"
    CLA="--debug"
else
    CLA=""
fi


python zephyr/server.py $CLA
