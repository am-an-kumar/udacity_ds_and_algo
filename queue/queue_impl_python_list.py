# this is a stripped off version of linked list that has all we need to implement a queue
class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        """
        Appends an element to the end of the queue
            :params: -
                value - value to append 
            :output: - None
        """
        self.list.append(value)

    def dequeue(self):
        """
        Removes the first element of a queue and returns it
            :params: - None
            :output: -
                value - value dequeued from queue
        """
        if len(self.list) == 0:
            return None
        return self.list.pop(0)

    def front(self):
        """
        Returns the first element of the queue 
            :params: - None
            :output: -
                value - value of the front most element of the queue
        """
        if len(self.list) == 0:
            return None
        return self.list[0]

    def size(self):
        """
        Returns the size of the queue
            :params: - None
            :output: -
                size - number of elements in queue
        """
        return len(self.list)

    def is_empty(self):
        """
        Returns if the queue is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the queue is empty
        """
        return len(self.list) == 0

    def __str__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        """
        if self.is_empty():
            return "Queue is empty"

        string_repr = "==============================\n         Front of queue         \n==============================\n"
        for item in self.list:
            string_repr += "{}\n".format(item)
        return string_repr

    def __repr__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        """
        return self.__str__()
