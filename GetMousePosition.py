#!/usr/bin/env python

# Mouse monitoring libary
from pynput.mouse import Listener
# import time
from time import sleep
from datetime import datetime

# Import other files in directory
import GetDimensions
from pfmqtt import Tx




class MouseMonitor:
    """

    GreyStarFish is a class that monitors curser clicks and provides the data for Purple Finch

    """

    def __init__(self):
        # Declare variables
        self.run = True
        self.data_list = []
        self.t = Tx("pfgs", "mqtt.eclipse.org", "lol")



    # Define on click
    def on_click(self, x, y, button, pressed):
        # Appends pressed and released position
        if pressed:
            data = (x, y, datetime.timestamp(datetime.now()))
            #self.data_list.append(data)
            self.t.send_unenc(str(data))
            print(data)


    def run_listener(self):
        # Start a listener thread
        listener = Listener(
            on_click=self.on_click
        )
        listener.start()
        # This needs to be on a specific time or something
        while self.run:
            sleep(10)  # Amount of time that the listner records the input.
            self.run = False
            # Stop listener
        listener.stop()

    def get_data(self):
        return self.data_list

    def emptyList(self):
        self.data_list.clear()

if __name__ == "__main__":
    myclass = MouseMonitor()
    myclass.run_listener()




