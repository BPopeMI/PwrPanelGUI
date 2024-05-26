# CyberPower PowerPanel Linux - (Gui)
This project provides a graphical user interface (GUI) to monitor the status of an CyberPower uninterruptible power supply (UPS) using the PowerPanel Linux software. The GUI is built with Python's tkinter library, offering a user-friendly way to retrieve and display UPS statistics, which are otherwise accessible only via terminal commands.

## Note
This project was to get back into the swings of python and linux. Its a very basic python script and currently redudant as the information is pulled from the terminal. If you like Gui, well here you go. End goal is to introduce similar functionality to the windows version with GUI configurable settings, etc.

* UPS used: 1500VA AVR

### Prerequisites
* [Python3](https://docs.python-guide.org/starting/install3/linux/) Language
* [tkinter](https://docs.python.org/3/library/tkinter.html) Gui library
* [setproctitle](https://pypi.org/project/setproctitle/) Process naming
* [PowerPanel Linux](https://www.cyberpowersystems.com/product/software/power-panel-personal/powerpanel-for-linux/) UPS


### Installing
* Install Prerequisites (Must - Unless you want to strip features)
* Clone the repository with [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=cli) or download the [zip](Insert Release link)
* Setting up [Sudoer](https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/)
```
sudo visudo
```
Add the following lines
```
#PwrPanel Project (Note comment this whatever you want.)
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/pwrstat
```

### Executing program

* Navigate to the install location in the terminal.
```
Python3 PwrPanel.py
```
Or to detach from the temrinal
```
nohup python3 PwrPanel.py &
```

## Version History
* 0.1
    * Intital Basic Release
* 0.2
    * New UI scaling ui
    * Automatically refreshes status every 5 seconds

## Issue Tracking
* Nothing I am aware of, besides general UI improvements & features.

## Ideal Features
* Cleaned up presentation
* Configurable settings
* Exporting/Importing settings
* Exporting Data
* Implement Widget with Plasma
* [matplotlib](https://matplotlib.org) Visualization library
