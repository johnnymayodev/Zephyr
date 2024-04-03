#! /bin/bash

if [ -d "venv" ]; then
    echo "Virtual environment already exists"
    echo "Clearing previous environment"
    rm -rf venv # Remove the virtual environment
fi


python3 -m venv venv


echo "Activating virtual environment"
source venv/bin/activate


echo "Updating pip"
pip install -q --upgrade pip


echo "Installing requirements"
pip install -q -r requirements.txt
