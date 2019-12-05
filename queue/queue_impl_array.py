class Queue:
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        """
        Appends an element to the end of the queue
            :params: -
                value - value to append 
            :output: - None
        Time complexity - O(n), {queue full will cause this worst case complexity}
        """
        # if queue is full, increase size
        if self.queue_size == len(self.arr):
            self.handle_full_capacity()

        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)

        # resetting front_index if it is the 1st enqueue
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        """
        Removes the first element of a queue and returns it
            :params: - None
            :output: -
                value - value dequeued from queue
        Time complexity - O(1)
        """
        # check if queue is empty
        if self.is_empty():
            # in case the queue got dequeued, the front_index pointing to 0 is fixed
            self.front_index = -1
            self.next_index = 0
            return None

        value = self.arr[self.front_index]
        # resetting to indicate that this index is vacant
        self.arr[self.front_index] = None
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def front(self):
        """
        Returns the first element of the queue 
            :params: - None
            :output: -
                value - value of the front most element of the queue
        Time complexity - O(1)
        """
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def handle_full_capacity(self):
        """
        Handles the case when queue gets full
            :params: - None
            :output: - None
        Time complexity - O(n)
        """
        old_arr = self.arr
        self.arr = [None for _ in range(len(old_arr) * 2)]

        index = 0

        # copying all elements from front index till the end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case when front_index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # resetting the pointers
        self.front_index = 0
        self.next_index = index

    def size(self):
        """
        Returns the size of the queue
            :params: - None
            :output: -
                size - number of elements in queue
        Time complexity - O(1)
        """
        return self.queue_size

    def is_empty(self):
        """
        Returns if the queue is empty
            :params: - None
            :output: -
                is_empty - (Boolean) True/False based on whether the queue is empty
        Time complexity - O(1)
        """
        return self.queue_size == 0

    def __str__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        Time complexity - O(x), here x is the capacity of array used to store the queue, even for n entries, the size is x where x>=n. 
        Worst case time complexity - O(2n)
        """
        if self.is_empty():
            return "Queue is empty"

        string_repr = "==============================\n         Front of queue         \n==============================\n"
        for item in self.arr:
            if item is not None:
                string_repr += "{}\n".format(item)
        return string_repr

    def __repr__(self):
        """
        Returns string representation of queue
            :params: - None
            :output: -
                string_repr - string representation of queue
        Time complexity - O(x), here x is the capacity of array used to store the queue, even for n entries, the size is x where x>=n. 
        Worst case time complexity - O(2n)
        """
        return self.__str__()
