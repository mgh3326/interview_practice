def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    result_list = input_list.copy()
    # Divide
    half_len = len(result_list) // 2
    left_list = merge_sort(result_list[half_len:])  # left
    right_list = merge_sort(result_list[:half_len])  # right
    # Conquer
    left_index = 0
    right_index = 0
    merged_list = []
    while True:
        if left_index == len(left_list):
            while True:
                if right_index == len(right_list):
                    break
                merged_list.append(right_list[right_index])
                right_index += 1
            break
        if right_index == len(right_list):
            while True:
                if left_index == len(left_list):
                    break
                merged_list.append(left_list[left_index])
                left_index += 1
            break
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
    return merged_list


print(
    merge_sort([1, 3, 2, 4, 5, 6, -1, -2, 0])
)
