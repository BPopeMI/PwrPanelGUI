# CyberPower PowerPanel Linux - (Gui)

This project provides a graphical user interface (GUI) to monitor the status of a CyberPower uninterruptible power supply (UPS) using the PowerPanel Linux software. The GUI is built with Python's tkinter library, offering a user-friendly way to retrieve and display UPS statistics, which are otherwise accessible only via terminal commands.

## Example

![Screenshot of what version 0.2a looks like. Very basic GUI frame with text outputting status](https://i.ibb.co/mHh9tht/Version-0-2a.png)

## Note

This project was to get back into the swings of python and linux. Its a very basic python script and currently redundant as the information is pulled from the terminal. If you like Gui, well here you go. End goal is to introduce similar functionality to the windows version with GUI configurable settings, etc. This DOES NOT alter the original source of PowerPanel Linux.

* UPS used: 1500VA AVR

### Prerequisites

* [Python3](https://docs.python-guide.org/starting/install3/linux/) Language
* [PowerPanel Linux](https://www.cyberpowersystems.com/product/software/power-panel-personal/powerpanel-for-linux/) UPS

### Installing

* Install Requirements (Use Pip on requirements.txt))
* Clone the repository with [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=cli) or download the [zip](Insert Release link)
* Setting up [Sudoer](https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/)

```bash
sudo visudo
```

Add the following lines

```text
#PwrPanel Project (Note comment this whatever you want.)
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/pwrstat
```

### Executing program

* Navigate to the install location in the terminal.

```bash
Python3 PwrPanel.py
```

Or to detach from the terminal

```bash
nohup python3 PwrPanel.py &
```

## Version History

* 0.1
* Initial Basic Release
* 0.2
* New UI scaling ui
* Automatically refreshes status every 5 seconds
* 0.2a
* Updated Icon image off stock tkinter
* 1.0 - Release
* Introduction of entire new UI
* Customizable status timeline

## Issue Tracking

## Ideal Features

* Cleaned up presentation
    * Rework UI layout
    * [matplotlib](https://matplotlib.org) Visualization library
    * Minimize/Hide GUI
* Configurable settings
* Exporting/Importing settings
* Exporting Data
* Implement Widget with Plasma

## Author/License/Notice

* This is entirely an opensource python project, that does not modify, adapt, translate, reverse engineer,
decompile, disassemble or otherwise attempt to discover the source code of all or
any part of the Power Panel software.
* All copy rights are resevered to their respective holders and intellectual property.
