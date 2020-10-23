import re
from screeninfo import get_monitors


def get_screen_size():
    width = 0
    height = 0
    for m in get_monitors():
        size = str(m)
    size = size.split(",")

    size = size[2] + " " + size[3]
    size = re.split('([0-9]+)', size)
    width = size[1]
    height = size[3]

    return int(width), int(height)
