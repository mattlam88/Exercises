def insert_element(array_num, ins_pos, ins_val):
    if array_num == []:
        return []
    array_num.insert(ins_pos, ins_val)
    return array_num

