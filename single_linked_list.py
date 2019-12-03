class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, list=None):
        """
        Creates a linked list with the elements of list as its nodes
            :params: - 
                list - the list to created linked list from
            :output: - None
        """
        self.head = None
        self.tail = None
        self.num_elements = 0

        # adding list items as nodes
        if list is not None:
            for list_item in list:
                self.append(list_item)

    def size(self):
        """ 
        Returns the size of list
        :params: - None
        :output: -
            -size - the number of nodes in the list
        Time complexity - O(1)
        """
        return self.num_elements

    def is_empty(self):
        """
        Returns if the list is empty
            :params: - None
            :output: - Boolean(True/False)
        Time complexity - O(1)
        """
        return self.num_elements == 0

    def to_list(self):
        """
        Returns the list representation of a linked list
        :params: - None
        :output:
            list - list representation of linked list
        Time complexity - O(n), assuming that append operation in python has a complexity of O(1)
        """
        list = []
        current_node = self.head
        while current_node is not None:
            list.append(current_node.value)
            current_node = current_node.next
        return list

    def append(self, value):
        """ 
        Inserts a node at the end
            :param:
                - value - the value of the new node
            :return: - None
        Time complexity - O(1)
        """
        # list is empty, both head and tail need to be updated
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        # list is not empty, only tail needs to be updated
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.num_elements += 1

    def prepend(self, value):
        """ 
        Inserts a node at the beginning
            :param:
                - value - the value of the new node
            :return: - None
        Time complexity - O(1)
        """
        # list is empty, both head and tail need to be updated
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        # list is not empty, only head needs to be updated
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp

        self.num_elements += 1

    def insert(self, index, value):
        """
        Inserts a node with specified value at specified index
            :params: -
                index - index where the node is to be inserted, if greater than size, the node is appended
                value - the value of the node to be inserted
            :output: - None
        Time complexity - O(n)
        """
        # if index is greater than size, we append, if it is less than 0, we prepend
        if index > self.num_elements-1:
            index = self.num_elements-1
        elif index < 0:
            index = 0

        # inserting the node
        if index == 0:
            return self.prepend(value)
        elif index == self.num_elements - 1:
            return self.append(value)
        else:
            counter = 1
            current_node = self.head
            while current_node.next is not None:
                if counter == index:
                    temp = current_node.next
                    current_node.next = Node(value)
                    current_node.next.next = temp
                    self.num_elements += 1
                    return
                counter += 1
                current_node = current_node.next

    def remove_from_end(self):
        """
        Removes the last node and returns its value
            :params: - None
            :output: - value of node removed and None if list is empty
        Time complexity - O(n)
        """
        if self.num_elements == 0:
            return None
        elif self.num_elements == 1:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            prev_node = self.head
            current_node = prev_node.next
            while current_node.next is not None:
                current_node = current_node.next
                prev_node = prev_node.next
            value = current_node.value
            prev_node.next = None
        self.num_elements -= 1
        return value

    def remove_from_beginning(self):
        """
        Removes the first node and retursn its value
            :params: - None
            :output: - value of node removed and None if the list is empty
        Time complexity - O(1)
        """
        if self.num_elements == 0:
            return None
        elif self.num_elements == 1:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next

        self.num_elements -= 1
        return value

    def remove(self, index):
        """
        Removes the node at specified index and returns its value
            :params: -
                index - the index of the node to remove
            :ouput: - value of the removed node and None if that index has no node
        Time complexity - O(n)
        """
        # adjusting index value
        if index > self.num_elements - 1:
            index = self.num_elements - 1
        elif index < 0:
            index = 0

        # removing the node
        if index == 0:
            return self.remove_from_beginning()
        elif index == self.num_elements - 1:
            return self.remove_from_end()
        else:
            counter = 1
            current_node = self.head
            while current_node.next is not None:
                if counter == index:
                    value = current_node.next.value
                    current_node.next = current_node.next.next
                    self.num_elements -= 1
                    return value
                current_node = current_node.next
                counter += 1

    def __str__(self):
        """
        Returns the string representation of a list
            :params: - None
            :output: - 
                value - (string) - string representation of list
        Time complexity - 
            self.to_list() to get list representation of list - O(n)
            str(item) for each list item - O(n)
            string.join() - O(n)
        overall ~= O(n)
        """
        return ", ".join([str(item) for item in self.to_list()])

    def search(self, value):
        """
        Checks whether a value is present in linked list
            :params: -
                value - the value to look for
            :output: -
                is_present(Boolean) - True/False based on whether the element was present
        Time complexity - O(n)
        """
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def get(self, index):
        """
        Returns the value of a node at a index, if not present, returns None
            :params: -
                index - the index of node whose value needs to be returned
            :output: -
                value - the value of node / None
        Time complexity - O(n)
        """
        if (index < 0) or (index > self.num_elements - 1):
            return None

        counter = 0
        current_node = self.head
        while current_node is not None:
            if index == counter:
                return current_node.value
            current_node = current_node.next
            counter += 1
        return None

    def __repr__(self):
        """
        Returns the string representation of the list by calling __str__()
        """
        return self.__str__()