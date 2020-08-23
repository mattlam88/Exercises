# Write your solution here
def reverse(string):
    if string == "":
        return ""
    return  string[-1] + reverse(string[:-1])
    