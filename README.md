# Signal Viewer App - Readme

## Overview
The Signal Viewer App is a graphical user interface (GUI) application developed using PyQt5 and Python. It allows users to view and analyze multiple moving signals using two graph widgets (channels). Each channel can plot multiple signals in different random colors or one chosen color. The app offers various features such as controlling each channel independently, linking channels together, and manipulating the signals in real-time.

## Team Information
The Signal Viewer App was created by Team 4, consisting of the following members:
- Sondos Mahmoud
- Fatma Ehab
- Mai Mohamed
- Noura Osama

## Features
The Signal Viewer App provides the following features:

### Channel Controls
- Show: Displays the selected channel.
- Hide: Hides the selected channel.
- Play: Starts the continuous movement of signals in the selected channel.
- Pause: Pauses the movement of signals in the selected channel.
- Reset: Resets the selected channel to its initial state.
- Zoom In: Zooms in on the signals in the selected channel.
- Zoom Out: Zooms out from the signals in the selected channel.
- Move Left: Shifts the signals in the selected channel to the left.
- Move Right: Shifts the signals in the selected channel to the right.
- Speed Up: Increases the movement speed of signals in the selected channel.
- Slow Down: Decreases the movement speed of signals in the selected channel.
![mash](https://github.com/sbme-tutorials/task1-signal-viewer-dsp_fall23_task1_team4/assets/115077795/42322912-f2ea-487b-8208-c5efaa519209)

### Keyboard Shortcuts
Each feature in the Signal Viewer App is associated with a keyboard shortcut for convenient access.
- open new file : "Ctrl+L"
- show : "Ctrl+E"
- hide :  "Ctrl+Y"
- save :  "Ctrl+S"
- clear : "Ctrl+Shift+D"
- play : "Ctrl+P"
- pause : "Ctrl+Shift+P"
- reset : "Ctrl+Shift+S"
- zoom in : "Up"
- zoom out : "Down"
- move right : "Right"
- move left : "Left"
- speed up : "Ctrl+F"
- slow down : "Ctrl+O"
### Channel Linking
The app allows the user to link the two channels together. When linked, manipulating one channel (e.g., zooming, shifting) will apply the same changes to the other channel.

### Signal Management
- Clean Channel: Clears all signals from the selected channel.
- Save as Screenshots: Saves the current state of the selected channel as screenshots in a PDF file named "report.pdf".

## Installation
To run the Signal Viewer App, follow these steps:

1. Install Python (version 3.7 or higher) if it is not already installed on your system.
2. Install the required dependencies by running the following command:
   ````shell
   pip install pyqt5
   ```
3. Download the Signal Viewer App source code from the repository.
4. Run main.py

## Usage
After launching the Signal Viewer App, you can perform the following actions:

1. Select a channel by clicking on the corresponding channel widget from the combobox.
2. Use the provided buttons or keyboard shortcuts to control the selected channel.
3. Link the channels together by checking the "Link Channels" option.
4. Manipulate the signals in the selected channel using the available features.
5. Clean a channel by clicking the "Clean Channel" button.
6. Save the current state of a channel as a PDF report by clicking the "Save" button.
