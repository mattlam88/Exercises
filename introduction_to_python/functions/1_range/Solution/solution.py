# Code your solution here
number = int(input())
def hundred_or_less(number):
    if number <= 100:
        solution = 'GREATNESS'
        return solution
    else:
        solution = "OOPS"
        return solution

result = hundred_or_less(number)
print(result)