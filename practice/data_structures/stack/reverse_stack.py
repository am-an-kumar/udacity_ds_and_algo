from stack_impl_linked_list import Stack


def reverse_stack(stack):
    """
    Returns the reversed stack
        :params: -
            stack - stack to be reversed
        :output: -
            stack -reversed stack
    Time complexity - O(n)
    """
    # one will be the reversed stack, and the other will be reversed again to maintain the original stack
    first_copy = Stack()
    second_copy = Stack()

    while not stack.is_empty():
        element = stack.pop()
        first_copy.push(element)
        second_copy.push(element)

    while not second_copy.is_empty():
        stack.push(second_copy.pop())

    return first_copy
