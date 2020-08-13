# Code your solution here
x = input()
def true_false(x):
    if x == True:
        data = "SHUTDOWN"
        return data
    else:
        data = "SHUTDOWN ABORTED"
        return data

result = true_false(x)
print(result)