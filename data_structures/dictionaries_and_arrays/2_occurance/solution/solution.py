def occurances(array_num, element):
    occur_num = 0
    for item in array_num:
        if element == item:
            occur_num += 1
    return occur_num
