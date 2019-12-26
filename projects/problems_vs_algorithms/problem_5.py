class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix=''):
        result = []
        if self.is_word and suffix != '':
            result.append(suffix)

        for char in self.children:
            result.extend(self.children[char].suffixes(suffix + char))
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

# getting reference to trie nodes to imitate that we have typed this much and autocomplete suggestions are based on what can come afterwards
an_trie_node = MyTrie.find("an")
fu_trie_node = MyTrie.find("fu")
fun_trie_node = MyTrie.find("fun")
all_possibilities = MyTrie.root

print(an_trie_node.suffixes())
# ['t', 'thology', 'tagonist', 'tonym']
print(fu_trie_node.suffixes())
# ['n', 'nction']
print(fun_trie_node.suffixes())
# ['ction']
print(all_possibilities.suffixes())
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
