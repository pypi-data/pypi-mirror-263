#!/bin/bash

echo "export PYTHONPATH=$PYTHONPATH:src" >> ~/.bashrc
pip3 install --user -r requirements.txt
