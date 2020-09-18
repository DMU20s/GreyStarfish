#!/usr/bin/env python

#Mouse monitoring libary
from pynput.mouse import Listener
import time

alldatalist = []
presseddatalist = []
releaseddatalist = []


#Define on click
def on_click(x, y, button, pressed):
    
    #Prints 
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

    #Appends pressed and released position
    alldatalist.append((x,y))
    
    
    

    # If this here. Only register one mouse click
    """if not pressed:
        # Stop listener
        return False"""

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
# Stop listener
listener.stop()



# Split pressed data and released data up into two different list. Both could possibly be used 
for i in range(len(alldatalist)):
    if i == 0 or i % 2 == 0:
        presseddatalist.append(alldatalist[i])
    else:
        releaseddatalist.append(alldatalist[i])


print(presseddatalist)

print(releaseddatalist)