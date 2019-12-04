class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, list = None):
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
            for item in list:
                self.append(item)

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
        Time complexity = O(n) assuming time complexity of list.append() is O(1)
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
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
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
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
        
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
        if index > (self.num_elements - 1):
            index = self.num_elements - 1
        elif index < 0:
            index = 0

        if index == 0:
            return self.prepend(value)
        elif index == self.num_elements - 1:
            return self.append(value)
        else:
            # as the counter = 0 case is already covered
            counter = 1
            # pointer to the second node
            current_node = self.head.next
            while current_node is not None:
                if index == counter:
                    # node before new node
                    next_node = current_node
                    # node after new node
                    prev_node = current_node.prev

                    # manipulating references
                    prev_node.next = Node(value)
                    prev_node.next.prev = prev_node
                    prev_node.next.next = next_node
                    next_node.prev = prev_node.next

                    # incrementing node count and returning
                    self.num_elements += 1
                    return

                counter += 1
                current_node = current_node.next

    def remove_from_end(self):
        """
        Removes the last node and returns its value
            :params: - None
            :output: - value of node removed and None if list is empty
        Time complexity - O(1)
        """
        if self.num_elements == 0:
            return None
        elif self.num_elements == 1:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.tail.value
            # storing a reference to the new tail node
            temp = self.tail.prev
            self.tail.prev = None
            self.tail = temp
            self.tail.next = None
        
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
            # storing a reference to the new head node
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.head.prev = None
        
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
        if index > (self.num_elements - 1):
            index = self.num_elements - 1
        elif index < 0:
            index = 0

        if index == 0:
            return self.remove_from_beginning()
        elif index == self.num_elements -1 :
            return self.remove_from_end()
        else:
            counter = 1
            current_node = self.head.next
            while current_node is not None:
                if index == counter:
                    value= current_node.value
                    prev_node = current_node.prev
                    next_node = current_node.next

                    prev_node.next = current_node.next
                    next_node.prev = current_node.prev

                    # not necessary
                    current_node.prev = None
                    current_node.next = None

                    # decrementing node count and returning the value of the removed node
                    self.num_elements -= 1
                    return value



    def __str__(self):
        """
        Returns the string representation of a list
            :params: - None
            :output: - 
                value - (string) - string representation of list
        Time complexity - O(n)
        """
        return ", ".join([str(item) for item in self.to_list()])

    def __repr__(self):
        """
        Returns the string representation of a list
            :params: - None
            :output: - 
                value - (string) - string representation of list
        Time complexity - O(n)
        """
        return self.__str__()

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
        return None
    
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

    def reverse(self):
        """
        Creates a new linked list that is reverse of the original one and returns its reference
            :params: - None
            :output: -
                ref - reference of newly created reversed linked list
        Time complexity - O(n)
        """
        new_list = DoublyLinkedList()
        current_node = self.tail
        while current_node is not None:
            new_list.append(current_node.value)
            current_node = current_node.prev

        return new_list


linked_list = DoublyLinkedList([1, 3, 5, 7])
print(linked_list.reverse())