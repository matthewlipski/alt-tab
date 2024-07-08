# AltTab for macOS
![AltTab Icon](./assets/icon512.png)

## Usage
This simple app allows for using the Alt+Tab hotkey to trigger the macOS app switching menu as well as the existing Cmd+Tab hotkey. The app runs entirely in the background, and does not add any menu bar or dock icons. Exiting requires finding AltTab in Activity Monitor and closing it from there. To run AltTab on startup, simply add it the the login items in System Preferences.

AltTab can be downloaded [here](https://github.com/matthewlipski/alt-tab/releases/tag/v1.0).

## Building from source
To build AltTab from source, you must first install the required packages using `pip`, either to a virtual environment or to your global site-packages:
```
pip install -r requirements.txt
```
To generate AltTab.app, run the following command:
```
python setup.py py2app
```
This will create two new directories, `build`, and `dist`. AltTab.app will be located in the `dist` directory.
