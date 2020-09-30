#!/bin/bash

# Setup local environment for Django

echo "Setting up development environment for FancyBin on Django"

ROOTDIR=$(dirname "$0")
if [ -d "$ROOTDIR/.venv" ]; then
  echo "Virtualenv already setup"
  exit 1
fi

echo "Creating virtualenv in .venv"
python3 -m venv $ROOTDIR/.venv

echo "Activating venv"
source $ROOTDIR/.venv/bin/activate

echo "Installing pip requirements in venv"
pip3 install -r $ROOTDIR/requirements.txt

echo "Done!"
