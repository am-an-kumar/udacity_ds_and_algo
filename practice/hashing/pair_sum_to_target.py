# Given an input_list and a target, return the indices of pair of integers in the list that sum to the target. The best solution takes O(n) time. You can assume that the list does not have any duplicates.

# For e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]


def pair_sum_to_target(input_list, target):
    """
    Returns a list of 2 indices of list, the sum of values of which equals target
        :params: -
            input_list - list to find indices in
            target - required sum of 2 elements
        :output: -
            [x, y] - list of indices
    Time complexity - O(n), where n = len(input_list)
    """
    # dictionary to store key-value pair from list, where key = value of list item for constant time lookup, value = index
    list_dict = dict()
    for index, value in enumerate(input_list):
        if (target - value) in list_dict:
            return [index, list_dict[target - value]]
        list_dict[value] = index

# code to test the implementation


def test_function(test_cases):
    for test_case in test_cases:
        output = pair_sum_to_target(test_case[0], test_case[1])
        if sorted(output) == test_case[2]:
            print("Pass")
        else:
            print("Fail")


test_function([
    [[1, 5, 9, 7], 8, [0, 3]],
    [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]],
    [[0, 1, 2, 3, -4], -4, [0, 4]]
])
