def bubble_sort(input_list):
    result_list = input_list.copy()
    for i in range(len(input_list)):
        for j in range(len(input_list))[:len(input_list) - i - 1]:
            if result_list[j] > result_list[j + 1]:
                temp_value = result_list[j + 1]
                result_list[j + 1] = result_list[j]
                result_list[j] = temp_value

    return result_list


print(
    bubble_sort([1, 3, 2, 4, 5, 6, -1, -2, 0])
)
