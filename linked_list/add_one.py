def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    Time complexity = O(n)
    """
    index = len(arr) - 1
    carry = 1

    while index >= 0:
        temp = arr[index] + carry
        arr[index] = temp % 10
        carry = temp // 10
        index -= 1

    if carry == 0:
        return arr
    else:
        return [carry] + arr


# code to test the implementation
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_cases = [
    [[0], [1]],
    [[1, 2, 3], [1, 2, 4]],
    [[1, 9, 9], [2, 0, 0]],
    [[9, 9, 9], [1, 0, 0, 0]],
]


for test_case in test_cases:
    test_function(test_case)
