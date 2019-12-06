def power_of_2(n):
    """
    Returns nth power of 2
        :params: - 
            n - number greater than on equal to 0
        :output: -
            value - 2^n
    Time complexity - 
    """
    if n == 0:
        return 1
    return 2 * power_of_2(n-1)
