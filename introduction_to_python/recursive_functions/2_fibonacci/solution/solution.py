# Write your solution here
def fibonacci(n):

    cache = dict()
    
    if n == 0:
        ans = 0
        cache[n] = ans
    elif n == 1 or n == 2:
        ans = 1
        cache[n] = ans

    if n in cache:
        return cache[n]

    elif n >= 3:
        ans = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = ans
    
    return ans

print(fibonacci(5))