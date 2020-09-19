#!/usr/bin/env python

# Mouse monitoring libary
from pynput.mouse import Listener
import time

# Import other files in directory
import GetDimensions


class MouseMonitor:
    """

    GreyStarFish is a class that monitors curser clicks and provides the data for Purple Finch

    """

    def __init__(self):
        # Declare variables

        self.alldatalist = []
        self.presseddatalist = []
        self.releaseddatalist = []
        self.test = True

        # Declare list storing data
        self.press_screen_one = []
        self.press_screen_two = []
        self.press_screen_three = []
        self.press_screen_four = []
        self.press_screen_five = []
        self.press_screen_six = []

    # Define on click
    def on_click(self, x, y, button, pressed):

        # Prints
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

        # Appends pressed and released position
        self.alldatalist.append((x, y))

        # If this here. Only register one mouse click
        """if not pressed:
            # Stop listener
            return False"""

    def run_listener(self):
        # Start a listener thread
        listener = Listener(
            on_click=self.on_click
        )
        listener.start()
        # This needs to be on a specific time or something
        while self.test:
            time.sleep(10)
            self.test = False
            # Stop listener
        listener.stop()
        self.split_data()
        self.collect_data()

    # Split pressed data and released data up into two different list. Both could possibly be used
    def split_data(self):

        for i in range(len(self.alldatalist)):
            if i == 0 or i % 2 == 0:
                self.presseddatalist.append(self.alldatalist[i])
            else:
                self.releaseddatalist.append(self.alldatalist[i])

    # Return data
    def get_data(self):

        # return self.presseddatalist, self.releaseddatalist
        return self.press_screen_one, self.press_screen_two, self.press_screen_three, self.press_screen_four, \
               self.press_screen_five, self.press_screen_six

    # Collect data
    def collect_data(self):
        width, height = GetDimensions.get_screen_size()

        for i in range(len(self.presseddatalist)):
            # Check height in the first if
            if 0 <= self.presseddatalist[i][1] <= height / 2:
                # Check if click is on screen 1 - 3 based on coordinates
                if 0 <= self.presseddatalist[i][0] <= width / 3.0:
                    self.press_screen_one.append(self.presseddatalist[i])
                elif width / 3.0 <= self.presseddatalist[i][0] <= 2 * (width / 3.0):
                    self.press_screen_two.append(self.presseddatalist[i])
                elif 2 * (width / 3.0) <= self.presseddatalist[i][0] <= width:
                    self.press_screen_three.append(self.presseddatalist[i])
            # Same as above just for screen 4 - 6 TODO BUGS Running Around here
            elif height / 2 <= self.presseddatalist[i][0] <= height:
                if 0 <= self.presseddatalist[i][0] <= width / 3:
                    print("Hello")
                    self.press_screen_four.append(self.presseddatalist[i])

                elif width / 3 <= self.presseddatalist[i][0] <= 2 * (width / 3):
                    self.press_screen_five.append(self.presseddatalist[i])
                    print("Hej")
                elif 2 * (width / 3) <= self.presseddatalist[i][0] <= width:
                    self.press_screen_six.append(self.presseddatalist[i])
                    print("Yo")


if __name__ == "__main__":
    myclass = MouseMonitor()
    myclass.run_listener()
    screen1, screen2, screen3, screen4, screen5, screen6 = myclass.get_data()
    print(screen1, "\n", screen2, "\n", screen3, "\n", screen4, "\n", screen5, "\n", screen6)
