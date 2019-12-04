class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                repr - string representation of a node
        Time complexity - O(1)
        """
        return "Node: {{value: {}, next: {}}}".format(self.value, self.next.value if self.next else None)

    def __repr__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                repr - string representation of a node
        Time complexity - O(1)
        """
        return self.__str__()

# this is a stripped off implementation of linked list. Just contains the APIs needed to implement a stack


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        """
        Pushes an element to the top of stack
            :params: -
                value - value to be inserted on top of stack
            :output: - None
        Time complexity - O(1)
        """
        # stack is empty
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        self.num_elements += 1

    def pop(self):
        """
        Removes the top element of a stack and returns it
            :params: - None
            :output: - 
                value - top element popped off the stack
        Time complexity - O(1)
        """
        # stack is empty
        if self.head is None:
            return None

        else:
            value = self.head.value
            self.head = self.head.next
            self.num_elements -= 1
            return value

    def top(self):
        """
        Returns the top element of the stack without removing it
            :params: - None
            :output - 
                value - top element of the stack
        Time complexity - O(1)
        """
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        """
        Returns the size of the stack
            :params: - None
            :output: -
                size - number of elements in the stack
        Time complexity - O(1)
        """
        return self.num_elements

    def is_empty(self):
        """
        Returns if the stack is empty
            :params: - None
            :output: -
                is_empty - (Boolean) Returns True/False based on whether the stack is empty
        Time complexity - O(1)
        """
        return self.head is None

    def __str__(self):
        """
        Returns the string representation of the linked list
            :params: - None
            :output: -
                repr - string representation of the list
        Time complexity - O(n)
        """
        if self.head is None:
            return "Stack is empty"
        else:
            string_repr = "==============================\n         Top of stack         \n==============================\n"
            current_node = self.head
            while current_node is not None:
                string_repr += "{}\n".format(current_node)
                current_node = current_node.next
            return string_repr

    def __repr__(self):
        """
        Returns the string representation of the linked list
            :params: - None
            :output: -
                repr - string representation of the list
        Time complexity - O(n)
        """
        return self.__str__()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)
