# Code your solution here
list_dup = ['a', 'a', 'a', 'n', 'z', 'e']

tot = 0
i = 0

while i < len(list_dup):
    if list_dup[i] == 'a':
        tot += 1
    i += 1

print(tot)