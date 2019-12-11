class Node:
    def __init__(self, value=None):
        """
        Initializes a Node object
            :params: -
                value - value of the node
            :output - None
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
        TIme complexity - O(1)
        """
        return self.left

    def get_right_child(self):
        """
        Returns the reference to the right child of a node
            :params: - None
            :output: -
                ref - reference to the right child / None if right child does not exist
        Time complexity - O(1)
        """
        return self.right

    def set_value(self, value):
        """
        Sets the value of a node
            :params: - 
                value - value of the node
            :output: - None
        Time complexity - O(1)
        """
        self.value = value

    def set_left_child(self, left):
        """
        Sets the reference of the left child of a node
            :params: -
                left - reference to the left child node
            :output: - None
        Time complexity - O(1)
        """
        self.left = left

    def set_right_child(self, right):
        """
        Sets the reference of the right child of a node
            :params: -
                right - reference to the right child of a node
            :output: - None
        Time complexity - O(1)
        """
        self.right = right

    def has_left_child(self):
        """
        Checks if the node has a left child
            :params: - None
            :output: -
                has_left_child: - True/False based on whether the node has a left child
        Time complexity - O(1)
        """
        return self.left is not None

    def has_right_child(self):
        """ 
        Checks if the node has a right child
            :params: - None
            :output: -
                has_right_child - True/False based on whether the node has a right child
        """
        return self.right is not None

    def __str__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time compelxity - O(1)
        """
        return "{{left: {}, value: {}, right: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)

    def __repr__(self):
        """
        Returns the string representation of a node
            :params: - None
            :output: -
                string_repr - string representation of a node
        Time compelxity - O(1)
        """
        return "{{left: {}, value: {}, right: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)

class Tree:
    def __init__(self, value=None):
        """
        Initializes a Tree object
            :params: -
                value - value of the root node of a tree
            :output - None
        Time compelxity - O(1)
        """
        self.root = Node(value)

    def get_root(self):
        """
        Returns the reference of the root node of a tree
            :params: - None
            :output: -
                ref - reference to the root node of a tree
        Time complexity - O(1)
        """
        return self.root

    def pre_order_traverse(self):
        """
        Traverses the binary tree in pre-order DFS manner
            :params: - None
            :output: -
                traversal_list - list with the order in which nodes of the tree were traversed
        Time complexity - O(n), because the loop will run n times, where n = number of nodes in tree. For every iteration, we do the one or more of the following operations like stack.push(), stack.pop(), current_node reassignment, all of which happens in constant time
        """
        stack = Stack()
        traversal_list = []
        root = self.get_root()

        if root is not None:
            current_node = root
            stack.push(current_node)

            while not stack.is_empty():

                # check if left subtree is traversed, if not traverse it
                if not stack.is_left_visited():

                    # adding node to traversal list
                    traversal_list.append(current_node.value)

                    # if the node has got no left child
                    if current_node.get_left_child() is None:
                        stack.set_left_visited()
                        continue

                    stack.set_left_visited()
                    current_node = current_node.get_left_child()
                    stack.push(current_node)

                    # check if right subtree is traversed, if not traverse it
                elif not stack.is_right_visited():

                    # adding node to traversal list
                    # traversal_list.append(current_node.value)

                    # if the node has got no right child
                    if current_node.get_right_child() is None:
                        stack.set_right_visited()
                        continue

                    stack.set_right_visited()
                    current_node = current_node.get_right_child()
                    stack.push(current_node)

                    # if both left and right subtree are traversed, pop the node from stack and set the current node as the new stack top
                else:
                    stack.pop()
                    current_node = stack.top()
                    if current_node is not None:
                        current_node = current_node["node"]

        return traversal_list

    def in_order_traverse(self):
        """
        Traverses the binary tree in in-order DFS manner
            :params: - None
            :output: -
                traversal_list - list with the order in which nodes of the tree were traversed
        Time complexity - O(n), because the loop will run n times, where n = number of nodes in tree. For every iteration, we do the one or more of the following operations like stack.push(), stack.pop(), current_node reassignment, all of which happens in constant time
        """
        stack = Stack()
        traversal_list = []
        root = self.get_root()

        if root is not None:
            current_node = root
            stack.push(current_node)

            while not stack.is_empty():

                # check if left subtree is traversed, if not traverse it
                if not stack.is_left_visited():

                    # adding node to traversal list
                    # traversal_list.append(current_node.value)

                    # if the node has got no left child
                    if current_node.get_left_child() is None:
                        stack.set_left_visited()
                        continue

                    stack.set_left_visited()
                    current_node = current_node.get_left_child()
                    stack.push(current_node)

                    # check if right subtree is traversed, if not traverse it
                elif not stack.is_right_visited():

                    # adding node to traversal list
                    traversal_list.append(current_node.value)

                    # if the node has got no right child
                    if current_node.get_right_child() is None:
                        stack.set_right_visited()
                        continue

                    stack.set_right_visited()
                    current_node = current_node.get_right_child()
                    stack.push(current_node)

                    # if both left and right subtree are traversed, pop the node from stack and set the current node as the new stack top
                else:
                    stack.pop()
                    current_node = stack.top()
                    if current_node is not None:
                        current_node = current_node["node"]

        return traversal_list

    def post_order_traverse(self):
        """
        Traverses the binary tree in post-order DFS manner
            :params: - None
            :output: -
                traversal_list - list with the order in which nodes of the tree were traversed
        Time complexity - O(n), because the loop will run n times, where n = number of nodes in tree. For every iteration, we do the one or more of the following operations like stack.push(), stack.pop(), current_node reassignment, all of which happens in constant time
        """
        stack = Stack()
        traversal_list = []
        root = self.get_root()

        if root is not None:
            current_node = root
            stack.push(current_node)

            while not stack.is_empty():

                # check if left subtree is traversed, if not traverse it
                if not stack.is_left_visited():

                    # adding node to traversal list
                    # traversal_list.append(current_node.value)

                    # if the node has got no left child
                    if current_node.get_left_child() is None:
                        stack.set_left_visited()
                        continue

                    stack.set_left_visited()
                    current_node = current_node.get_left_child()
                    stack.push(current_node)

                    # check if right subtree is traversed, if not traverse it
                elif not stack.is_right_visited():

                    # adding node to traversal list
                    # traversal_list.append(current_node.value)

                    # if the node has got no right child
                    if current_node.get_right_child() is None:
                        stack.set_right_visited()
                        continue

                    stack.set_right_visited()
                    current_node = current_node.get_right_child()
                    stack.push(current_node)

                    # if both left and right subtree are traversed, pop the node from stack and set the current node as the new stack top
                else:
                    stack.pop()
                    # adding node to traverse list
                    traversal_list.append(current_node.value)

                    current_node = stack.top()
                    if current_node is not None:
                        current_node = current_node["node"]

        return traversal_list

    def __str__(self):
        """
        Returns the string representation of a tree
            :params: - None
            :output: -
                string_repr - in-order traversal list for tree
        Time complexity - O(n)
        """
        return self.in_order_traverse()

    def __repr__(self):
        """
        Returns the string representation of a tree
            :params: - None
            :output: -
                string_repr - in-order traversal list for tree
        Time complexity - O(n)
        """
        return self.in_order_traverse()

class Stack:
    def __init__(self):
        """
        Initializes a stack object
            :params: - None
            :output - None
        Time complexity - O(1)
        """
        self.data = []

    def push(self, node):
        """
        Pushes a node on top of stack
            :params: -
                node - node of tree to push on top of stack
            :output: - None
        Time complexity - O(1), as complexity of list.append() in python is O(1)
        """
        self.data.append({
            "left_visited": False,
            "node": node,
            "right_visited": False
        })

    def pop(self):
        """
        Pops the top of the stack
            :params: - None
            :output - 
                node - node popped from stack / None if stack is empty
        Time complexity - O(1), as complexity of list.pop() in python is O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def top(self):
        """
        Returns the top element of stack without popping it
            :params: - None
            :output: -
                top_node - reference to the top node of stack / None if the stack is empty
        Time complexity - O(1)
        """
        if len(self.data) == 0:
            return None
        return self.data[len(self.data) - 1]

    def size(self):
        """
        Returns the size of stack
            :params: - None
            :output: -
                size - number of elements in stack
        Time complexity - O(1)
        """
        return len(self.data)

    def is_empty(self):
        """
        Checks if stack is empty
            :params: - None
            :output: -
                is_empty - True/False based on whether the stack is empty
        """ 
        return self.size() == 0

    def is_left_visited(self):
        """
        Checks if the topmost node of stack has visited left subtree
            :params: - None
            :output: -
                is_left_visited - True/False based on whether the left subtree of topmost node of stack is visited
        Time complexity - O(1)
        """
        if self.size() == 0:
            return None
        return self.data[len(self.data) - 1]["left_visited"]

    def is_right_visited(self):
        """
        Checks if the topmost node of stack has visited right subtree
            :params: - None
            :output: -
                is_right_visited - True/False based on whether the right subtree of the topmost node of stack is visited
        Time complexity - O(1)
        """
        if self.size() == 0:
            return None
        return self.data[len(self.data) - 1]["right_visited"]

    def set_left_visited(self):
        """
        Marks the left subtree of the topmost node as visited
            :params: - None
            :output: - None
        Time complexity - O(1)
        """
        if self.size() == 0:
            return
        self.data[len(self.data) - 1]["left_visited"] = True

    def set_right_visited(self):
        """
        Marks the right subtree of the topmost node as visited
            :params: - None
            :output: - None
        Time complexity - O(1)
        """
        if self.size() == 0:
            return
        self.data[len(self.data) - 1]["right_visited"] = True

    def __str__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                string_repr - string representation of stack
        Time complexity - O(n), where n = size of stack
        """
        if self.is_empty():
            return "Stack is empty"
        string_repr = "Top of stack\n===================\n"
        for item in self.data:
            string_repr += "{{left_visited: {}, node: {}, right_visited: {}}}".format(item["left_visited"], item["node"], item["right_visited"])
        return string_repr

    def __repr__(self):
        """
        Returns the string representation of stack
            :params: - None
            :output: -
                string_repr - string representation of stack
        Time complexity - O(n), where n = size of stack
        """
        if self.is_empty():
            return "Stack is empty"
        string_repr = "Top of stack\n===================\n"
        for item in self.data:
            string_repr += "{{left_visited: {}, node: {}, right_visited: {}}}".format(item["left_visited"], item["node"], item["right_visited"])
        return string_repr


# lets create a tree manually for now, since we have not created method to insert nodes into a tree
tree = Tree("1")
tree.get_root().set_left_child(Node("2"))
tree.get_root().set_right_child(Node("3"))
tree.get_root().get_left_child().set_left_child(Node("4"))
tree.get_root().get_left_child().set_right_child(Node("5"))
tree.get_root().get_right_child().set_left_child(Node("6"))
tree.get_root().get_right_child().set_right_child(Node("7"))
tree.get_root().get_right_child().get_right_child().set_left_child(Node("8"))
tree.get_root().get_right_child().get_right_child().get_left_child().set_left_child(Node("9"))
print(tree.pre_order_traverse())
print(tree.in_order_traverse())
print(tree.post_order_traverse())

print()

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(tree.pre_order_traverse())
print(tree.in_order_traverse())
print(tree.post_order_traverse())


stack = Stack()
stack.push(Node("5"))
print(stack)