def reverse_string(input):
    """
    Reverses a string using recursion
        :params: -
            input - input string to reverse
        :output: -
            rev_str - reversed input string
    Time complexity - O(n*k) where k is the size of sub-string ~ O(n^2)
    """
    if len(input) == 0:
        return ""
    return reverse_string(input[1:]) + input[0]
