def sum_integers_recursive(n):
    """
    Returns the sum of first n integers
        :params: -
            n - integer ( n >= 1 )
        :output: -
            sum - (1 + 2 + .... + n)
    Time complexity - O()
    """
    if n == 1:
        return 1
    return n + sum_integers_recursive(n-1)


def sum_integers(n):
    """
    Returns the sum of first n integers
        :params: -
            n - integer ( n >= 1 )
        :output: -
            sum - (1 + 2 + .... + n)
    Time complexity - O(1)
    """
    return (n * (n+1))//2
