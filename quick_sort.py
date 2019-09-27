def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    result_list = input_list.copy()
    # Divide
    pivot_index = 0
    pivot_value = result_list[pivot_index]
    left_list = []
    right_list = []
    for i in range(len(result_list)):
        if i == pivot_index:
            continue
        if result_list[i] < pivot_value:
            left_list.append(result_list[i])
        else:
            right_list.append(result_list[i])
    left_list = quick_sort(left_list)
    right_list = quick_sort(right_list)
    merge_list = []
    merge_list.extend(left_list)
    merge_list.append(pivot_value)
    merge_list.extend(right_list)
    return merge_list


print(
    quick_sort([1, 3, 2, 4, 5, 6, -1, -2, 0])
)
