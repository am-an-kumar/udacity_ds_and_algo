class RouterTrieNode:
    def __init__(self):
        self.sub_paths = {}
        self.handler = None

    def insert(self, sub_path):
        if sub_path not in self.sub_paths:
            self.sub_paths[sub_path] = RouterTrieNode()


class RouterTrie:
    def __init__(self, root_handler):
        self.root = RouterTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        current_node = self.root

        for sub_path in path:
            current_node.insert(sub_path)
            current_node = current_node.sub_paths[sub_path]

        current_node.handler = handler

    def find(self, path):
        current_node = self.root

        for sub_path in path:
            if sub_path not in current_node.sub_paths:
                return None
            current_node = current_node.sub_paths[sub_path]

        return current_node.handler


class Router:
    def __init__(self, root_handler, four_o_four_handler):
        self.router = RouterTrie(root_handler)
        self.four_o_four_handler = four_o_four_handler

    def add_handler(self, path_string, handler):
        path = self._split_path(path_string)
        self.router.insert(path, handler)

    def lookup(self, path_string):
        path = self._split_path(path_string)

        if len(path) == 0:
            return self.router.handler

        handler = self.router.find(path)

        if handler is not None:
            return handler
        else:
            return self.four_o_four_handler

    def _split_path(self, path_string):
        return [sub_path for sub_path in path_string.split('/') if sub_path != '']


# unit test cases

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# some lookups with the expected output
print(router.lookup("/"))
# 'root handler'
print(router.lookup("/home"))
# 'not found handler'
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/about/"))
# 'about handler'
print(router.lookup("/home/about/me"))
# 'not found handler'
