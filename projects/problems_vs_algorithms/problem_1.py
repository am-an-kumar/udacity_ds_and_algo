def sqrt(number):
    """
    Calculate the floored square root of a number
        Args:
            number(int): Number to find the floored squared root
        Returns:
            int: Floored Square Root/ None for invalid input
    Time complexity - O(log(n))
    """
    if not isinstance(number, int) or number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    start = 0
    end = number // 2

    while start <= end:
        mid = (start + end) // 2
        mid_squared = mid * mid

        if mid_squared == number:
            return mid

        elif mid_squared < number:
            start = mid + 1
            ans = mid

        else:
            end = mid - 1
    return ans


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt("added edge cases")) else "Fail")
print("Pass" if (None == sqrt(None)) else "Fail")
print("Pass" if (None == sqrt(-27)) else "Fail")
