# GreyStarfish
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A data provider for PurpleFinch.
Gathers mouse cursor coordinates, and submits them to PurpleFinch.


Check the PurpleFinch WIKI for protocol drafts...

Overview:

main.py is the script that runs greystarfish and its functionality.

pfmqtt.py is the scrift that transmit the data from greystarfish to PF (Purple Finch).

get_positions.py is the skeleton of greystarfish. This is where alle the data gets captured

Setup:

To run GreyStarFish you need to install the following python libraries:

- pynput - https://pypi.org/project/pynput/
- screeninfo - https://pypi.org/project/screeninfo/

Note that GreyStarFish is written in python 3.8.5. This means that it is not compatible with python 2

GreyStarfish is compatible with Windows and Linux Ubunto 20.04. Tested 10/03/20. Not Mac 

Run:

Option 1:
- Open main.py in the python IDE or another IDE with python 3.8 installed
- Run main.py

Option 2:
- Locate the greystarfish directory in the terminal or CMD prompt
- Run the main with "python3 main.py"



Sources: 

https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

https://pynput.readthedocs.io/en/latest/

Made by:
- [Emil "0xcyber-sketch" Langager Larsen](https://github.com/0xcyber-sketch)


