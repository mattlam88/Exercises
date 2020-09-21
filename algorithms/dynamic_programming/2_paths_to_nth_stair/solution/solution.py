def paths_nth_stair(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:    
        return paths_nth_stair(n-2) + paths_nth_stair(n-1)



