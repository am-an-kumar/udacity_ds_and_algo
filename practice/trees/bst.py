class Node:
    def __init__(self, value=None):
        """
        Initialsizes a node object
            :params: -
                value - value of the node
            :output: - None
        Time complexity - O(1)
        """
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        """
        Returns the value of a node
            :params: - None
            :output: -
                value - value of the node
        Time complexity - O(1)
        """
        return self.value

    def get_left_child(self):
        """
        Returns the reference to the left child of a node
            :params: - None
            :output: -
                ref - reference to the left child / None if left child does not exist
        Time complexity - O(1)
        """
        return self.left

    def get_right_child(self):
        """
        Returns the reference to the right child of a node
            :params: - None
            :output: -
                reff - reference to the right child / None if right child does not exist
        """
        return self.right

    def set_value(self, value):
        """ 
        Sets the value of a node
            :params: -
                value - value to set on the node
            :output: - None
        Time complexity - O(1)
        """
        self.value = value

    def set_left_child(self, ref):
        """
        Sets the left child of a node
            :params: -
                ref - reference to the new left child of the node
            :output: - None
        Time complexity - O(1)
        """
        self.left = ref

    def set_right_child(self, ref):
        """
        Sets the right child of a node
            :params:  -
                ref - reference to the new right child of the node
            :output - None
        Time complexity - O(1)
        """
        self.right = ref

    def has_left_child(self):
        """
        Checks if a node has a left child
            :params: - None
            :output: -
                has_left_child - True/False based on whether the node has a left child
        Time complexity - O(1)
        """
        return self.left is not None

    def has_right_child(self):
        """ 
        Checks if a node has a right child
            :params: - None
            :output: -
                has_right_child - True/False based on whether the node has a right child
        Time complexity - O(1)
        """
        return self.right is not None

    def __str__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of the node
        Time complexity - O(1)
        """
        return "{{ left_child: {}, value: {}, right_child: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)

    def __repr__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of the node
        Time complexity - O(1)
        """
        return "{{ left_child: {}, value: {}, right_child: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)


class BST:
    def __init__(self, value=None):
        """
        Initializes a BST object
            :params: - 
                value - value of the root node
            :output: - None
        Time complexity - O(1)
        """
        self.root = Node(value)
        # root node is created when tree is created
        self.num_elements = 1

    def get_root(self):
        """
        Returns the reference to the root node
            :params: - None
            :output: -
                ref - reference to the root node
        Time complexity - O(1)
        """
        return self.root

    
    def traverse(self):
        """
        Returns a list traversed in ascending order,  i.e. in-order traversed
            :params: - None
            :output: -
                traverse_list - list with order in which nodes were traversed
        Time complexity - O()
        """

    def reverse_traverse(self):
        """
        Returns a list traversed in descending order, i.e. RNL order
            :params: - None
            :output: -
                traverse_list - list with order in which nodes were traversed
        Time complexity - O()
        """

    def search(self, value):
        """
        Searches the tree for a value
            :params: -
                value - value to search for
            :output: -
                node - node with value match / None if no match is found
        Time complexity - O()
        """

    def insert(self, value):
        """
        Inserts a node in the tree with passed value
            :params: -
                value - value of node to insert, no insertion happens if node with passed value is already present in the tree
            :output: - None
        Time complexity - 
            Average case - O(log n)
            Worst case - O(n)
        """
        root = self.get_root()
        current_node = root

        # if the root node has a value of None, then inserting a node won't make any sense
        if root is not None:
            while True:
                node_value = current_node.get_value()

                # no insertion
                if value == node_value:
                    print("Node already exists")
                    return

                # left subtree insertion
                elif value < node_value:                 
                    # if the current node has no left child, create a new node and make it the left child of the current node
                    if not current_node.has_left_child():
                        current_node.set_left_child(Node(value))
                        self.num_elements += 1
                        return
                    # else go left
                    current_node = current_node.get_left_child()

                # right subtree insertion
                else:
                    # if the current node has no right child, create a new node and make it the right child of the current node
                    if not current_node.has_right_child():
                        current_node.set_right_child(Node(value))
                        self.num_elements += 1
                        return
                    # else go right
                    current_node = current_node.get_right_child()



    def delete(self, value):
        """
        Removes the node in the tree with passed value
            :params: -
                value - value to look for
            :output: - node removed / None if node not found
        Time complexity - O()
        """

    def size(self):
        """
        Returns the number of nodes in the tree
            :params: - None
            :output: - 
                size - number of nodes in the tree
        Time complexity - O(1)
        """
        return self.num_elements

    def is_empty(self):
        """
        Checks if the tree is empty
            :params: - None
            :output: - 
                is_empty - True/False based on whether the tree is empty or not
        Time complexity - O(1)
        """
        return self.num_elements == 0

    def __str__(self):
        """
        Returns the string representation of the tree
            :params: - None
            :output: -
                string_repr - string representation of the tree
        Time complexity - O()
        """

    def __repr__(self):
        """
        Returns the string representation of the tree
            :params: - None
            :output: -
                string_repr - string representation of the tree
        Time complexity - O()
        """

print("Just checking!!!")