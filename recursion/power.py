def power_of_2(n):
    """
    Returns nth power of 2
        :params: - 
            n - exponent greater than on equal to 0
        :output: -
            value - 2^n
    Time complexity - O(n)
    """
    if n == 0:
        return 1
    return 2 * power_of_2(n-1)


def power_of_x(x, n):
    """
    Returns nth power of x
        :params: - 
            x - number
            n - exponent greater than on equal to 0
        :output: -
            value - x^n
    Time complexity - O(n)
    """
    if n == 0:
        return 1
    return x * power_of_x(x, n-1)


def pow(x, n):
    """
    Return x raised to n
        :params: - 
            x - number
            n - exponent(integer)
        :output: -
            value - x^n(x raised to n)
    Time complexity - O(mod(n))
    """
    if n == 0:
        return 1
    elif n < 0:
        return 1/pow(x, -n)
    return x * pow(x, n-1)
