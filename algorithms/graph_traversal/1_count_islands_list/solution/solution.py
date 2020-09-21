def count_islands(adjacency_list):
    count = 0
    for key, value in adjacency_list.items():
        print(key, value)
        if value == []:
            count += 1
    return count

adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3],
    4: [],
    5: [6],
    6: [3,5]
}

count_islands(adjacency_list)