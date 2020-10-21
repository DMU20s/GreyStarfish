from GetDimensions import get_screen_size


def get_region(xy_coordinates):
    width, height = get_screen_size()
    region_one = []
    region_two = []
    region_three = []
    region_four = []
    region_five = []
    region_six = []


    for i in range(len(xy_coordinates)):
        # Check height in the first if
        if 0 <= xy_coordinates[i][1] <= height / 2:
            # Check if click is on region 1 - 3 based on coordinates
            if 0 <= xy_coordinates[i][0] <= width / 3.0:
                region_one.append(xy_coordinates[i])

            elif width / 3.0 <= xy_coordinates[i][1] <= 2 * (width / 3.0):
                region_two.append(xy_coordinates[i])

            elif 2 * (width / 3.0) <= xy_coordinates[i][1] <= width:
                region_three.append(xy_coordinates[i])
        # Same as above just for region 4 - 6
        elif height / 2 <= xy_coordinates[i][1] <= height:
            if 0 <= xy_coordinates[i][1] <= width / 3.0:
                region_four.append(xy_coordinates[i])

            elif width / 3.0 <= xy_coordinates[i][1] <= 2 * (width / 3.0):
                region_five.append(xy_coordinates[i])

            elif 2 * (width / 3.0) <= xy_coordinates[i][1] <= width:
                region_six.append(xy_coordinates[i])

    return region_one, region_two , region_three , region_four, region_five, region_six