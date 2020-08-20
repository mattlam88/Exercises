# Code your solution here
def count_even(*args):
    count = 0
    for arg in args:
        if arg % 2 == 0:
            count += 1
    return count