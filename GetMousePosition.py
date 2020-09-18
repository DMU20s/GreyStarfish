#!/usr/bin/env python

#Mouse monitoring libary
from pynput.mouse import Listener
import time

datalist = []

#Define on click
def on_click(x, y, button, pressed):
    global datalist
    #Prints 
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

    #Appends pressed and released position
    datalist.append((x,y))
    
    
    

    # If this here. Only register one mouse click
    if not pressed:
        # Stop listener
        return False

test = True
if __name__ == "__main__":
    pass

# Start a listener thread
listener = Listener(
    on_click=on_click)



listener.start()

while test:
    time.sleep(10)
    test = False

listener.stop()

print(datalist[0])

print(datalist[1])


