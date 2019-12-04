class Stack:
    def __init__(self, initialSize=10):
        self.arr = [None for _ in range(initialSize)]
        self.capacity = initialSize
        self.next_index = 0

    def push(self, value):
        """
        Pushes a value on top of the stack
            :params: - 
                value - the value to be put on top of stack
            :output: - None
        Time complexity - O(n), O(1) in general, but for cases when the array used to store the data is full, the time complexity will be O(n)
        """
        if self.next_index >= self.capacity:
            self.increase_capacity()

        self.arr[self.next_index] = value
        self.next_index += 1

    def pop(self):
        """
        Removes the top element of the stack and returns it
            :params: - None
            :output: -
                value - Element removed from the top of stack
        Time complexity - O(1)
        """
        if self.next_index == 0:
            return None

        # getting the value and setting the placeholder to None
        value = self.arr[self.next_index - 1]
        self.arr[self.next_index - 1] = None
        self.next_index -= 1
        return value

    def size(self):
        """
        Returns the element count of stack
            :params: - None
            :output: -
                size - number of elements in stack
        Time complexity - O(1)
        """
        return self.next_index

    def is_empty(self):
        """
        Returns if the stack is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the stack is empty
        Time complexity - O(1)
        """
        return self.next_index == 0

    def top(self):
        """
        Returns the top element of the stack without removing it
            :params: - None
            :output: -
                value - top element of the stack
        Time complexity - O(1)
        """
        if self.next_index == 0:
            return None
        return self.arr[self.next_index - 1]

    def increase_capacity(self):
        """
        Doubles the capacity of the stack and copies the previous elements into the new array
            :params: - None
            :output: - None
        Time complexity - O(n)
        """
        self.arr = self.arr + [None for _ in range(self.capacity)]
        self.capacity *= 2

    def __str__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                repr - (string) representation of stack
        Time complexity - O(n)
        """
        if len(self.arr) == 0:
            return "Stack is empty"
        else:
            string_rep = "====================\n    Top of Stack    \n===================="
            for item in reversed(self.arr):
                if item is not None:
                    string_rep += "\n{}".format(item)
            return string_rep

    def __repr__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                repr - (string) representation of stack
        Time complexity - O(n)
        """
        return self.__str__()

print("Just checking...")