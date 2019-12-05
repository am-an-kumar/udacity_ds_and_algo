from stack_impl_linked_list import Stack


def evaluate_postfix(input_list):
    """
    Evaluates the postfix expression and returns the result
        :params: -
            input_list - list of operators/operands
        :output: -
            answer - evalutate postfix expression
    Time complexity - O(n)
    """
    stack = Stack()
    for item in input_list:
        if item == "+":
            second_operand = int(stack.pop())
            first_operand = int(stack.pop())
            stack.push(first_operand + second_operand)
        elif item == "-":
            second_operand = int(stack.pop())
            first_operand = int(stack.pop())
            stack.push(first_operand - second_operand)
        elif item == "*":
            second_operand = int(stack.pop())
            first_operand = int(stack.pop())
            stack.push(first_operand * second_operand)
        elif item == "/":
            second_operand = int(stack.pop())
            first_operand = int(stack.pop())
            stack.push(int(first_operand / second_operand))
        else:
            stack.push(item)

    return stack.pop()


def test_function(test_case):
    output = evaluate_postfix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)