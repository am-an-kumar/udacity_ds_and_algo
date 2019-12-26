import random


def get_min_max(input_list):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = input_list[0]
    min = input_list[0]

    for number in input_list:
        if number > max:
            max = number
        if number < min:
            min = number
    return (min, max)


# unit test cases
l = [i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [-i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if ((-9, 0) == get_min_max(l)) else "Fail")

l = [0 for i in range(100)]
random.shuffle(l)
print("Pass" if ((0, 0) == get_min_max(l)) else "Fail")
