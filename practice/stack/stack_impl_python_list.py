class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        """
        Pushes a value on top of the stack
            :params: - 
                value - the value to be put on top of stack
            :output: - None
        """
        self.list.append(value)

    def pop(self):
        """
        Removes the top element of the stack and returns it
            :params: - None
            :output: -
                value - Element removed from the top of stack
        """
        if len(self.list) == 0:
            return None
        return self.list.pop()

    def size(self):
        """
        Returns the element count of stack
            :params: - None
            :output: -
                size - number of elements in stack
        """
        return len(self.list)

    def is_empty(self):
        """
        Returns if the stack is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the stack is empty
        """
        return len(self.list) == 0

    def top(self):
        """
        Returns the top element of the stack without removing it
            :params: - None
            :output: -
                value - top element of the stack
        """
        if len(self.list) == 0:
            return None
        return self.list[0]

    def __str__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                repr - (string) representation of stack
        """
        if len(self.list) == 0:
            return "Stack is empty"
        else:
            string_rep = "====================\n    Top of Stack    \n====================\n"
            for item in self.list:
                string_rep += "{}\n".format(str(item))
            return string_rep

    def __repr__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                repr - (string) representation of stack
        """
        return self.__str__()

