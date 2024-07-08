#!/bin/bash

rm -rf dist
rm -rf build
source venv/bin/activate
python3 setup.py py2app
