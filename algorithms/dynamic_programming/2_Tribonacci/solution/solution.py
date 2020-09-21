def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if  n == 2 or n ==3:
        return 1
    return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)