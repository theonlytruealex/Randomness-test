#! /bin/bash

# create the virtual env
python3 -m venv .venv

# activate the venv 
source ./.venv/bin/activate

# install tkinter on linux
sudo apt-get install python3-tk

# install the required packages
python3 -m pip install -r requirements.txt

# run 
python3 ./src/gui.py
