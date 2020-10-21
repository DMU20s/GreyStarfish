#!/usr/bin/env python
from pynput.mouse import Listener
# import time
from time import sleep
from datetime import datetime
import threading

# Import other files in directory
from pfmqtt import Tx

import json


class MouseMonitor:
    """

    GreyStarFish is a class that monitors cursor clicks and provides the data for Purple Finch

    """

    def __init__(self):
        # Declare variables
        self.run = True
        self.data_list = []
        self.t = Tx("d6f73930-cd18-4021-b28a-1d9a3e733333/6bfc17fb-3c55-4a29-81e7-c55089134ace", "mqtt.eclipse.org",
                    "lol")

    # Define on click
    def on_click(self, x, y, button, pressed):
        # Appends pressed and released position
        if pressed:
            # Captures data and converts it to json
            data = json.dumps({"x": x, "y": y, "timestamp": datetime.timestamp(datetime.now())})
            self.data_list.append(data)

    def send_thread(self):
       # if len(self.data_list) > 0:

        #self.t.send_unenc(str(self.data_list))
        print(self.data_list)
        self.data_list.clear()
        self.send_thread()

    def run_listener(self):
        # Start a listener thread
        sender = threading.Timer(2, self.send_thread)
        sender.start()
        listener = Listener(
            on_click=self.on_click
        )
        listener.start()
        #sender.cancel()
        # This needs to be on a specific time or something
        while self.run:
            sleep(10)  # Amount of time that the listener records the input.
            self.run = False
            # Stop listener
        listener.stop()

# import threading
# def printit():
#  threading.Timer(5.0, printit).start()
#  print("Hello, World!")
