def insert_sort(input_list):
    result_list = input_list.copy()
    for i in range(len(input_list))[1:]:
        current_index = i
        current_value = result_list[current_index]
        while True:
            if current_index == 0 or current_value >= result_list[current_index - 1]:
                break
            result_list[current_index] = result_list[current_index - 1]
            current_index -= 1
        result_list[current_index] = current_value
    return result_list


print(
    insert_sort([1, 3, 2, 4, 5, 6, -1, -2, 0])
)
