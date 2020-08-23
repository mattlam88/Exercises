# Write your solution here
def custom_sort(num_list):

    if len(num_list) <= 1:
        return num_list
    elif len(num_list) >= 2:
        middle = len(num_list) // 2
        left = num_list[:middle]
        right = num_list[middle:]

        custom_sort(left)
        custom_sort(right)

        # index for left half
        i = 0
        # index for right half
        j = 0
        
        # index for entire num_list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1
        return num_list



