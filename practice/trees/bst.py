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

# to be used for DFS traversal of tree
class Stack:
    def __init__(self):
        """
        Initializes a stack object
            :params: - None
            :output: - None
        Time complexity - O(1)
        """
        self.data = []
    
    def push(self, node):
        """
        Pushes a node on top of stack
            :params: - 
                node - node to be inserted on top of stack
            :output: - None
        Time complexity - O(1)
        """
        self.data.append({
            'left_visited': False,
            'node': node,
            'right_visited': False
        })

    def pop(self):
        """
        Removes and returns the topmost element of stack
            :params: - None
            :output: -
                node - node popped / None if stack is empty
        Time complexity - O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def top(self):
        """
        Returns the topmost element of stack without removing it
            :params: - None
            :output: -
                node - topmost node of stack / None if stack is empty
        Time complexity - O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data[len(self.data) - 1]

    def size(self):
        """
        Returns the size of the stack
            :params: - None
            :output: -
                size - size of the stack
        Time complexity - O(1)
        """
        return len(self.data)
    
    def is_empty(self):
        """
        Checks if stack is empty
            :params: - None
            :output: -
                is_empty - True/False based on whether the stack is empty
        Time complexity - O(1)
        """
        return len(self.data) == 0

    def is_left_visited(self):
        """
        Checks if the left child is visited for the topmost node of stack
            :params: - None
            :output: -
                is_left_visited - True/False based on whether the left child of topmost node of stack is visted
        Time complexity - O(1)
        """
        return self.data[len(self.data) - 1] ["left_visited"]

    def is_right_visited(self):
        """
        Checks if the right child is visited for the topmost node of stack
            :params: - None
            :output: -
                is_right_visited - True/False based on whether the right child is visited for the topmost node of stack
        Time complexity - O(1)
        """
        return self.data[len(self.data) - 1] ["right_visited"]

    def set_left_visited(self):
        """
        Marks the left child visited for the topmost node of stack
            :params: - None
            :output: - None
        Time complexity - O(1)
        """
        self.data[len(self.data) - 1] ["left_visited"] = True

    def set_right_visted(self):
        """
        Marks the right child visited for the topmost node of stack
            :params: - None
            :outupt: - None
        Time complexity - O(1)
        """
        self.data[len(self.data) - 1] ["right_visited"] = True

    def __str__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                string_repr - String representation of stack

        Time complexity - O(n)
        """
        if self.size() == 0:
            return "Stack is empty"
        string_repr = "Top of stack\n==================\n"
        for item in reversed(self.data):
            string_repr += "{{left_visited: {}, node: {}, right_visited: {}}}\n".format(item["left_visited"], item["node"], item["right_visited"])
        return string_repr

    def __repr__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                string_repr - String representation of stack

        Time complexity - O(n)
        """
        if self.size() == 0:
            return "Stack is empty"
        string_repr = "Top of stack\n==================\n"
        for item in reversed(self.data):
            string_repr += "{{left_visited: {}, node: {}, right_visited: {}\n}}".format(item["left_visited"], item["node"], item["right_visited"])
        return string_repr

# to be used for BFS traversal of tree
class Queue:
    def __init__(self):
        """
        Initializes a queue object
            :params: - None
            :output: - None
        Time complexity - O(1)
        """
        self.data = []

    def enqueue(self, node):
        """
        Appends a node to the end of the queue
            :params: -
                node - node to enqueue
            :output: - None
        Time complexity - O(1)
        """
        self.data.append(node)

    def dequeue(self):
        """
        Removes the first element of queue
            :params: - None
            :output: -
                node - dequeued node of stack / None if queue is empty
        Time complexity - O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

    def front(self):
        """
        Returns the first element of queue without removing it
            :params: - None
            :output: -
                node - first element of queue / None if queue is empty
        Time complexity - O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data[0]

    def size(self):
        """
        Returns the size of queue
            :params: - None
            :output: -
                size - number of elements in stack
        Time complexity - O(1)
        """
        return len(self.data)

    def is_empty(self):
        """
        Checks if a queue is empty
            :params: - None
            :output: -
                is_empty - True/False based on whether the queue is empty
        Time complexity - O(1)
        """
        return len(self.data) == 0

    def __str__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time complexity - O(n)
        """
        if self.size() == 0:
            return "Queue is empty"
        string_repr = "Front of Queue\n==================\n"
        for node in self.data:
            string_repr += "{}\n".format(node)
        return string_repr

    def __repr__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time complexity - O(n)
        """
        if self.size() == 0:
            return "Queue is empty"
        string_repr = "Front of Queue\n==================\n"
        for node in self.data:
            string_repr += "{}\n".format(node)
        return string_repr

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
        Time complexity - O(n)
        """
        root = self.get_root()
        traverse_list = []
        stack = Stack()

        if root is not None:
            stack.push(root)
            while not stack.is_empty():
                current_node = stack.top()["node"]

                # visiting left subtree if not visited already
                if not stack.is_left_visited():
                    # if left is None, mark it visited
                    if not current_node.has_left_child():
                        stack.set_left_visited()

                    # else visit it
                    else:
                        stack.set_left_visited()
                        stack.push(current_node.get_left_child())
                        continue


                # visiting right subtree if not visited already
                if not stack.is_right_visited():
                    # if right is None, mark it visited
                    if not current_node.has_right_child():
                        traverse_list.append(current_node.value)
                        stack.set_right_visted()

                    # else visit it
                    else:
                        traverse_list.append(current_node.value)
                        stack.set_right_visted()
                        stack.push(current_node.get_right_child())
                        continue

                # popping the node from stack if both left and right subtree is visited
                if stack.is_left_visited() and stack.is_right_visited():
                    stack.pop()

        return traverse_list

    def reverse_traverse(self):
        """
        Returns a list traversed in descending order, i.e. RNL order
            :params: - None
            :output: -
                traverse_list - list with order in which nodes were traversed
        Time complexity - O(n)
        """
        root = self.get_root()
        traverse_list = []
        stack = Stack()

        if root is not None:
            stack.push(root)
            while not stack.is_empty():
                current_node = stack.top()["node"]

                # visiting right subtree if not visited already
                if not stack.is_right_visited():
                    # if right is None, mark it visited
                    if not current_node.has_right_child():
                        stack.set_right_visted()

                    # else visit it
                    else:
                        stack.set_right_visted()
                        stack.push(current_node.get_right_child())
                        continue


                # visiting left subtree if not visited already
                if not stack.is_left_visited():
                    # if left is None, mark it visited
                    if not current_node.has_left_child():
                        traverse_list.append(current_node.value)
                        stack.set_left_visited()

                    # else visit it
                    else:
                        traverse_list.append(current_node.value)
                        stack.set_left_visited()
                        stack.push(current_node.get_left_child())
                        continue

                # popping the node from stack if both left and right subtree is visited
                if stack.is_left_visited() and stack.is_right_visited():
                    stack.pop()

        return traverse_list

    def level_traverse(self):
        """ 
        Returns a list of nodes traversed in level order from left to right
            :params: - None
            :output: -
                traverse_list - list with level order left to right traversal
        Time complexity - O()
        """

    def search(self, value):
        """
        Searches the tree for a value
            :params: -
                value - value to search for
            :output: -
                is_present - True/False based on whether the node is found
        Time complexity - 
            Average complexity - O(log n)
            Worst complexity - O(n)
        """
        root = self.get_root()
        current_node = root

        while current_node is not None:
            node_value = current_node.get_value()

            # node found
            if value == node_value:
                return True

            # node may be in the left subtree
            if value < node_value:
                current_node = current_node.get_left_child()

            # node may be in the right subtree
            if value > node_value:
                current_node = current_node.get_right_child()

        return False

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
        Time complexity - O(n)
        """
        return self.traverse()

    def __repr__(self):
        """
        Returns the string representation of the tree
            :params: - None
            :output: -
                string_repr - string representation of the tree
        Time complexity - O(n)
        """
        return self.traverse()

tree = BST(10)
items = [5, -1, -3, 9, 0, 13, 17, 14, 12]
for item in items:
    tree.insert(item)


for item in items:
    print(tree.search(item))

print(tree.traverse())
print(tree.reverse_traverse())


