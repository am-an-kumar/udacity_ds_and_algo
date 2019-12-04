def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    Time complexity: O(n)
    """
    expected_sum = 0
    actual_sum = 0
    length = len(arr)
    for index, number in enumerate(arr):
        if index != length - 1:
            expected_sum += index
        actual_sum += number
    return actual_sum - expected_sum


# code to test the implementation
def test_function(test_case):
    arr = test_case[0]
    expected_output = test_case[1]
    output = duplicate_number(arr)

    if expected_output == output:
        print("Pass")
    else:
        print("Fail")


test_cases = [
    [[0,0], 0],
    [[0, 2, 3, 1, 4, 5, 3], 3],
    [[0, 1, 5, 4, 3, 2, 0], 0],
    [[0, 1, 5, 5, 3, 2, 4], 5]
]

for test_case in test_cases:
    test_function(test_case)