#!/bin/bash

# Activate virtualenvironment for licence_manager

ROOTDIR=$(pwd)

# must be sourced
(return 0 2>/dev/null) && sourced=1 || sourced=0
if [ $sourced -ne 1 ]; then
  echo "This script must be sourced"
  exit 1
fi

echo "Checking for virtual environment."
if [ ! -d "$ROOTDIR/.venv" ]; then
  echo "No virtualenv found at .venv, run localdevbootstrap.sh to set this up"
  return 1
fi

python3 -c 'import sys; exit(0) if ((hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix))) else exit(1)'
if [ $? -eq 0 ]; then
  echo "Already in .venv"
else
    echo "Sourcing .venv/bin/activate."
    source $ROOTDIR/.venv/bin/activate
fi