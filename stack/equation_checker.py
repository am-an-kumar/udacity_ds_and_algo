from stack_impl_linked_list import Stack


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    Time complexity - O(n)
    """
    stack = Stack()
    for literal in equation:
        if literal == "(":
            stack.push(literal)
        elif literal == ")":
            if stack.top() == "(":
                stack.pop()
            else:
                return False

    if stack.size() == 0:
        return True
    return False


print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
