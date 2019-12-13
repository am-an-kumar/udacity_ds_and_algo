def factorial(n):
    """
    Calculate n!
        :params: -
            n - number to find factorial of
        :output: -
            value - n!
    Time complexity - O(n)
    """
    if n == 0:
        return 1
    return n * factorial(n-1)
