from setuptools import setup

APP = ['main.py']  # points to your main python file
DATA_FILES = []
OPTIONS = {
    'iconfile': 'assets/icon.icns',
    'packages': ['Quartz', 'pynput'],  # include your other dependencies here
    'plist': {
        'LSBackgroundOnly': True
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    name="AltTab",
    options={
        'py2app': OPTIONS
    },
    setup_requires=['py2app'],
    version="1.0"
)
