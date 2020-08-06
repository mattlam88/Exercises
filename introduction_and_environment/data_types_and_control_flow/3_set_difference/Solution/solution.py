# Code your solution here
set_1 = "Hello World"
set_2 = "Hello Universe"

i = 0
result = []
while i < len(set_1):
    if set_1[i] in set_2:
        result.append(set_1[i])
    i += 1
print(result)