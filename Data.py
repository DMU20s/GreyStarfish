def create_data():
    with open("Data.txt", "w") as f:
        f.write()


def add_data(list1, list2, list3, list4, list5, list6):
    temp = [list1, list2, list3, list4, list5, list6]

    for i in temp:
        help_add_data(i)
        with open("data.txt", "a+") as f:
            f.write(" Total coordinate sets " + str(len(i)))
            f.write(" | ")


def help_add_data(list1):
    if len(list1) == 0:
        pass
    else:
        for i in range(len(list1)):
            with open("data.txt", "a+") as f:
                f.write(str(list1[i]))


def empty_data():
    with open ("data.txt", "w") as f:
        f.truncate(0)
