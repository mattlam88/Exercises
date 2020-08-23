# Write your solution here
def factorial_recursive(n):
    cache = dict()

    if n == 0 or n == 1:
        result = 1
        cache[n] = result

    if n in cache:
        return cache[n]    
    
    if n >= 2:
        result = n * factorial_recursive(n - 1)
        cache[n] = result
        return result
