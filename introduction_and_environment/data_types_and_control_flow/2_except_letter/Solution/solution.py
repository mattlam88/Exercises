# Code your solution here
vowels = ['A', 'E', 'I', 'O', 'U']
string = "BYTE ACADEMY"

i = 0
data = []

while i < len(string):
    if string[i] not in vowels:
        data.append(string[i])
    i += 1
print(data)

