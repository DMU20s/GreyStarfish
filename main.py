#!/usr/bin/env python

from os import path

import GetMousePosition
from Data import add_data, empty_data



if __name__ == "__main__":
    recorded_list = []
    my_class = GetMousePosition.MouseMonitor()
    my_class.run_listener()
    screen1, screen2, screen3, screen4, screen5, screen6 = my_class.get_data()

    add_data(screen1, screen2, screen3, screen4, screen5, screen6)
    #empty_data()





