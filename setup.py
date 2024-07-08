#!/usr/bin/env python3

from setuptools import setup

setup(
    app=['src/main.py'],
    data_files=[],
    name="Optab",
    options={
        'py2app': {
            'iconfile': 'assets/icon.icns',
            'packages': ['Quartz', 'pynput'],
            'plist': {
                'LSUIElement': True,
                'LSBackgroundOnly': True
            }
        }
    },
    setup_requires=['py2app'],
    version="1.0"
)
