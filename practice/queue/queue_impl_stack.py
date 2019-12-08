from stack_impl_linked_list import Stack


class Queue:
    def __init__(self):
        self.in_storage = Stack()
        self.out_storage = Stack()

    def enqueue(self, value):
        """
        Appends an element to the end of the queue
            :params: -
                value - value to append 
            :output: - None
        Time complexity - O(1)
        """
        self.in_storage.push(value)

    def dequeue(self):
        """
        Removes the first element of a queue and returns it
            :params: - None
            :output: -
                value - value dequeued from queue
        Time complexity - O(n)
        """
        if self.out_storage.size() == 0:
            while not self.in_storage.is_empty():
                self.out_storage.push(self.in_storage.pop())

        return self.out_storage.pop()

    def front(self):
        """
        Returns the first element of the queue 
            :params: - None
            :output: -
                value - value of the front most element of the queue
        Time complexity -O(n)
        """
        if self.out_storage.size() == 0:
            while not self.in_storage.is_empty():
                self.out_storage.push(self.in_storage.pop())

        return self.out_storage.top()

    def size(self):
        """
        Returns the size of the queue
            :params: - None
            :output: -
                size - number of elements in queue
        Time complexity - O(1)
        """
        return self.in_storage.size() + self.out_storage.size()

    def is_empty(self):
        """
        Returns if the queue is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the queue is empty
        Time complexity - O(1)
        """
        return self.size() == 0
