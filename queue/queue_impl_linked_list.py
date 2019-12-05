class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        """
        Returns string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time complexity - O(1)
        """
        return "Node: {{value: {}, next: {}}}".format(self.value, self.next.value if self.next else None)

    def __repr__(self):
        """
        Returns string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time complexity - O(1)
        """
        return self.__str__()


# this is a stripped off version of linked list that has all we need to implement a queue
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        """
        Appends an element to the end of the queue
            :params: -
                value - value to append 
            :output: - None
        Time complexity - O(1)
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.num_elements += 1

    def dequeue(self):
        """
        Removes the first element of a queue and returns it
            :params: - None
            :output: -
                value - value dequeued from queue
        Time complexity - O(1)
        """
        if self.head is None:
            return None

        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.num_elements = 0
            return value

        value = self.head.value
        self.num_elements -= 1
        self.head = self.head.next
        return value

    def front(self):
        """
        Returns the first element of the queue 
            :params: - None
            :output: -
                value - value of the front most element of the queue
        Time complexity - O(1)
        """
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        """
        Returns the size of the queue
            :params: - None
            :output: -
                size - number of elements in queue
        Time complexity - O(1)
        """
        return self.num_elements

    def is_empty(self):
        """
        Returns if the queue is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the queue is empty
        Time complexity - O(1)
        """
        return self.num_elements == 0

    def __str__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        Time complexity - O(n)
        """
        if self.head is None:
            return "Queue is empty"

        current_node = self.head
        string_repr = "==============================\n         Front of queue         \n==============================\n"
        while current_node is not None:
            string_repr += "{}\n".format(current_node)
            current_node = current_node.next
        return string_repr

    def __repr__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        Time complexity - O(n)
        """
        return self.__str__()
