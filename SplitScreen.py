#!/usr/bin/env python

import GetDimensions

width, height = GetDimensions.get_screen_size()

screens = {"screen_one": [(0, width / 3.00), (0, height / 2.00)],
           "screen_two": [(0, width / 3.00), (height / 2.00, height)],
           "screen_three": [(width / 3.00, 2 * (width / 3.00)), (0, height / 2.00)],
           "screen_four": [(width / 3.00, 2 * (width / 3.00)), (height / 2.00, height)],
           "screen_five": [(2 * (width / 3.00), width), (0, height / 2.00)],
           "screen_six": [(2 * (width / 3.00), width), (height / 2.00, height)]

}

print(screens)