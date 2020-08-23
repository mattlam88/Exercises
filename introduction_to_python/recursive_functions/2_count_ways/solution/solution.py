# Write your solution here
def print_list_of_list(lst):
    for item in lst:
        print(item)

def count_ways(steps):
    if steps == 1:
        return [[1]]
    if steps == 2:
        steps_num = count_ways(1)
        steps_num[0].append(1)
        
        steps_num.append([2])
        return steps_num
    

    x = count_ways(steps-1)
    for item_1 in x:
        item_1.append(1)
    # print_list_of_list(x)

    y = count_ways(steps - 2)
    for item_2 in y:
        item_2.append(2)

    return x + y


stairs = count_ways(5)
print_list_of_list(stairs)

