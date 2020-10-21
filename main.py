#!/usr/bin/env python


import GetMousePosition
import  getRegions
from pfmqtt import Tx

from Data import add_data, empty_data




if __name__ == "__main__":
    my_class = GetMousePosition.MouseMonitor()
    my_class.run_listener()


    #t = Tx("pfgs", "mqtt.eclipse.org", "lol")
    #t.send_unenc(str()


    #print(my_class.get_data())
    #getRegions.get_region(my_class.get_data())


    #add_data(screen1, screen2, screen3, screen4, screen5, screen6)
    #empty_data()




