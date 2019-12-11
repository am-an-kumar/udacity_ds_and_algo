class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __str__(self):
        return "{{left: {}, value: {}, right: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)

    def __repr__(self):
        return "{{left: {}, value: {}, right: {}}}".format(self.left.value if self.left else None, self.value, self.right.value if self.right else None)


# ????????????????????????????
# we will have to handle the case where Tree() is called without passing the value for root node
# ????????????????????????????
class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def pre_order_traverse(self):
        """
        Traverses the binary tree in pre-order DFS manner
            :params: - None
            :output: -
                traversal_list - list with the order in which nodes of the tree were traversed
        Time complexity - O()
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
        Time complexity - O()
        """

    def post_order_traverse(self):
        """
        Traverses the binary tree in post-order DFS manner
            :params: - None
            :output: -
                traversal_list - list with the order in which nodes of the tree were traversed
        Time complexity - O()
        """


class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append({
            "left_visited": False,
            "node": node,
            "right_visited": False
        })

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def top(self):
        if len(self.data) == 0:
            return None
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def is_left_visited(self):
        if self.size() == 0:
            return None
        return self.data[len(self.data) - 1]["left_visited"]

    def is_right_visited(self):
        if self.size() == 0:
            return None
        return self.data[len(self.data) - 1]["right_visited"]

    def set_left_visited(self):
        if self.size() == 0:
            return
        self.data[len(self.data) - 1]["left_visited"] = True

    def set_right_visited(self):
        if self.size() == 0:
            return
        self.data[len(self.data) - 1]["right_visited"] = True


# lets create a tree manually for now, since we have not created method to insert nodes into a tree
# tree = Tree("1")
# tree.get_root().set_left_child(Node("2"))
# tree.get_root().set_right_child(Node("3"))
# tree.get_root().get_left_child().set_left_child(Node("4"))
# tree.get_root().get_left_child().set_right_child(Node("5"))
# tree.get_root().get_right_child().set_left_child(Node("6"))
# tree.get_root().get_right_child().set_right_child(Node("7"))
# print(tree.pre_order_traverse())

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(tree.pre_order_traverse())
