class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix=''):
        result = []

        # if we are at the text that user typed, and it is a word itself, then we add it to result and look for it's children
        if self.is_word and suffix != '':
            result.append(suffix)

        # if it is a leaf node
        if len(self.children) == 0:
            return result

        for char in self.children:
            result.extend(self.children[char].suffixes(suffix=suffix+char))

        return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Adds a word to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Checks if a word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node


# unit test code
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def test_function(trie_node, word_list):
    if trie_node is None:
        return word_list == []
    else:
        return trie_node.suffixes() == word_list


print("Pass" if test_function(MyTrie.find("an"), [
      't', 'thology', 'tagonist', 'tonym']) else "Fail")
print("Pass" if test_function(MyTrie.find("fu"), ['n', 'nction']) else "Fail")
print("Pass" if test_function(MyTrie.find("fun"), ['ction']) else "Fail")
print("Pass" if test_function(MyTrie.find("ant"), ['hology', 'agonist', 'onym']) else "Fail")
print("Pass" if test_function(MyTrie.root, ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']) else "Fail")
print("Pass" if test_function(MyTrie.find("you can't find me"), []) else "Fail")
