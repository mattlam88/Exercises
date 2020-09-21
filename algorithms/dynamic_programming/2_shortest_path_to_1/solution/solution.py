def shortest_path_to_1(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n > 3:
        count = 0
        while n > 1:
            if n%3 == 0 and n%2 == 0:
                n = n//3
            elif n%3 == 0:
                n = n//3
            elif n%2 == 0:
                n = n//2
            else:
                n = n - 1
            count += 1
        return count
            
assert shortest_path_to_1(1) ==0
assert shortest_path_to_1(2) ==1
assert shortest_path_to_1(3) ==1
assert shortest_path_to_1(4) ==2
assert shortest_path_to_1(5) == 3
assert shortest_path_to_1(10) == 3


