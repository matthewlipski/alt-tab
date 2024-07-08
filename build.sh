#!/bin/bash

rm -rf build
rm -rf dist
source venv/bin/activate
python3 setup.py py2app
