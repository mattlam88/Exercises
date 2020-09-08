def get_child_nodes(heap, index):
    left_index = index*2 + 1
    right_index = index*2 + 2
    child_lst = []
    if left_index < len(heap):
        child_lst.append(heap[left_index])
    if right_index < len(heap):
        child_lst.append(heap[right_index])
    return child_lst