# Code your solution here
def div_by_3(*args):
    div3 = list(filter((lambda x: not x % 3),args))
    return div3