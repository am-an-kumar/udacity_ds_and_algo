class Node(object):
    """Node for a double linked list"""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):
    def __init__(self, size):
        self.size = size
        self.num_elements = 0
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.set_head(node)
            return node.value
        return -1

    def set(self, key, value):
        if self.num_elements == self.size:
            self.remove_LRU()
        new_node = Node(value)
        self.cache[key] = new_node
        self.set_head(new_node)
        self.num_elements += 1

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            if self.head.prev == None:
                self.tail = self.head
            self.head = node

    def remove_node(self, node):
        if self.num_elements == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.prev
            self.head.next = None
        elif node == self.tail:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def remove_LRU(self):
        node = self.tail
        del self.cache[node.value]
        self.remove_node(node)
        self.num_elements -= 1

    def __str__(self):
        if self.head is None:
            return "LRU cache is empty"

        string = "Least Recently Used\n====================\n"
        current_node = self.tail
        while current_node is not None:
            string += "{}\n".format(current_node.value)
            current_node = current_node.next
        return string + "Most Recently Used\n===================="


# Tests

our_cache = LRU_Cache(5)

print(our_cache)
# "LRU cache is empty"

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(9))
# -1, because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
# will remove 3 from cache
our_cache.set(7, 7)
# will remove 4 from cache

print(our_cache.get(3))
# -1
print(our_cache.get(4))
# -1


print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(5))
# 5

our_cache.set(9, 9)
# removes 6
our_cache.set(8, 8)
# removes 7

print(our_cache.get(6))
# -1
print(our_cache.get(6))
# -1

print(our_cache)
# Least Recently Used
# ====================
# 1
# 2
# 5
# 9
# 8
# Most Recently Used
# ====================
