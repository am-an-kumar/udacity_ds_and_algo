def rotated_array_search_recursive(input_list, number, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = input_list[mid_index]

    if mid_element == number:
        return mid_index

    # as the sorted array is rotated, we search in both half instead of one half as in case of binary search. One will return -1, the other some index, we return the index
    index_left_search = rotated_array_search_recursive(
        input_list, number, start_index, mid_index - 1)
    index_right_search = rotated_array_search_recursive(
        input_list, number, mid_index + 1, end_index)

    return max(index_left_search, index_right_search)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
