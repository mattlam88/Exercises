# Code your solution here
data = []
x = 50
for num in range(0,x):
    if num % 5 == 0 or num % 7 == 0:
        data.append(num)
print(data)
