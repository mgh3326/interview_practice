def select_sort(input_list):
    result_list = input_list.copy()
    for i in range(len(input_list)):
        min_index = i
        for j in range(len(input_list))[i + 1:]:
            if result_list[j] < result_list[min_index]:
                min_index = j
        if min_index != i:
            result_list[i], result_list[min_index] = result_list[min_index], result_list[i]
    return result_list


print(
    select_sort([1, 3, 2, 4, 5, 6, -1, -2, 0])
)
