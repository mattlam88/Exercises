def frequency_array(lst):
    max_num = max(lst)
    count = 0
    for i in range(0, max_num):
        for x in len(lst):
            if x == i:
                count += 1
        
    return
