from stack_impl_linked_list import Stack


def minimum_bracket_reversals(input_string):
    """
    Calculates the minimum number of reversals to fix the brackets
        :params: -
            input_string - (string) string of brackets
        :output: -
            count - number of reversals required to fix the brackets
    """
    if len(input_string) % 2 != 0:
        return -1
    count = 0
    stack = Stack()
    for bracket in input_string:
        if bracket == "{":
            stack.push(bracket)
        else:
            if stack.top() == "{":
                stack.pop()
            else:
                count += 1
                stack.push("{")

    if stack.size() == 0:
        return count
    else:
        return stack.size() // 2


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_1)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_3)
