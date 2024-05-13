# Recorder-defect-inspection
Final project in completing robotics and Artificial Engineering Undergraduate degree.  
This is a python-based project using PySide6 (PyQt) instance as GUI designer and  
used a serial Communication between Arduino and python.

## Running The Program
Clone this repo and type into your terminal
> `python -u main.py`

## Editing the GUI function
***Before further editing, please understand the PySide6 Documentation*** [HERE](https://doc.qt.io/qtforpython-6/) <br />
1. to edit how the program run, proceed to use `mainwindow.py`
2. carefully examine the widget name within the ui file, either with:
   > 1. using PyQt Designer (type `PySide6-Designer` into your terminal and open `main.ui` file)<br />
   > 2. or look through the `mainWindow.ui` file and search the widget class declaration

<br />
<br />

### Notes:
1. **MVSDK** is a default library to connect the machine vision camera with the program.
2. Program would run just fine without you having the machine vision camera, as long as you have a default built-in camera in your machine
3. The Ui file should not be change directly, because everything would be back to as it is even if you change the content of the file
4. **SDKtools** is a custom class for camera function usage for main app ***which utilize MVSDK library***
5. 
