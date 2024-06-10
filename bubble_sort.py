def bubble_sort(list_of_values):
    for max_index in range(len(list_of_values), 0, -1):
        for index in range(1, max_index):
            list_of_values[index-1], list_of_values[index] = sorted([list_of_values[index], list_of_values[index - 1]])
    return list_of_values


print(bubble_sort([2, 4, 1, 5, 2, 5, 2, 4, 2, 6,]))
