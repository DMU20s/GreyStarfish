#!/usr/bin/env python

import GetMousePosition

if __name__ == "__main__":
    myclass = GetMousePosition.MouseMonitor()
    myclass.run_listener()
    screen1, screen2, screen3, screen4, screen5, screen6 = myclass.get_data()
    print(screen1, "\n", screen2, "\n", screen3, "\n", screen4, "\n", screen5, "\n", screen6)