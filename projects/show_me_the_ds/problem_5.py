import hashlib
import time


class Block:
    def __init__(self, timestamp, data, prev_hash):
        """
        Initializes a blockchain block
            :params: -
                timestamp(time) - time in GMT when the block was created
                data(string) - data of block
                prev_hash(string) - string
                prev(ref) - reference of previous Node / None
            :output: - None
        Time complexity - O(n), where n = size of data to hash
        """
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        """
        Calculates the hash encoding of a string using SHA256
            :params: - None
            :output: -
                hash_value(string) - hash value of the data of a block
        Time complexity - O(n), where n = size of data to hash
        """
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        """
        Returns the string representation of a block
            :params: - None
            :output: -
                string_repr(str) - string representation of a block
        Time complexity - O(1)
        """
        return "Block\n=================\nTime stamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}".format(self.timestamp, self.data, self.prev_hash, self.hash)

    def __repr__(self):
        """
        Returns the string representation of a block
            :params: - None
            :output: -
                string_repr(str) - string representation of a block
        Time complexity - O(1)
        """
        return "Block\n=================\nTime stamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}".format(self.timestamp, self.data, self.prev_hash, self.hash)


class BlockChain:
    def __init__(self):
        """
        Creates a blockchain instance
            :params: -
            :output: -
        Time complexity - O(1)
        """
        self.head = None
        self.tail = None
        self.num_blocks = 0

    def add_block(self, data):
        """
        Adds a block to a blockchain
            :params: - 
                data(string) - data of the block
            :output: - None
        Time complexity - O(n), where n = length of data, as it calls Block()
        """
        timestamp = time.gmtime()
        # when blockchain is empty
        if self.head is None:
            self.head = Block(timestamp, data, prev_hash = 0)
            self.tail = self.head

        # when blockchain ain't empty, appending to the end
        else:
            temp = Block(timestamp, data, prev_hash = self.tail.hash)
            temp.prev = self.tail
            self.tail = temp

        self.num_blocks += 1

    def size(self):
        """
        Returns the size of a blockchain
            :params: - None
            :output: -
                size(number) - number of blocks in a blockchain
        Time complexity - O(1)
        """
        return self.num_blocks

    def is_empty(self):
        """
        Checks if a blockchain is empty
            :params: - None
            :output: -
                is_empty(Boolean) - True/False based on whether a blockchain is empty or not
        Time complexity - O(1)
        """
        return self.num_blocks == 0

    def __str__(self):
        """
        Returns the string representation of a blockchain
            :params: - None
            :output: -
                string_repr(string): string representation of blockchain
        Time complexity - O(n), where n = number of blocks in blockchain, as __str__ of Block has linear complexity, i.e. O(1)
        """
        if self.tail is None:
            return "Blockchain is empty"

        else:
            string_repr = ""
            current_node = self.tail
            while current_node is not None:
                string_repr += "{}\n".format(current_node)
                current_node = current_node.prev
            return string_repr

    def __repr__(self):
        """
        Returns the string representation of a blockchain
            :params: - None
            :output: -
                string_repr(string): string representation of blockchain
        Time complexity - O(n), where n = number of blocks in blockchain, as __str__ of Block has linear complexity, i.e. O(1)
        """
        return self.__str__()

    def search_block(self, data):
        """
        Searches the blockchain for a block with certain data
            :params: -
                data(string) - data to search for in block chain
            :output: - 
                block(Block) - True if found, else False
        Time complexity - O(n), where n = no of blocks in blockchain
        """
        # data present in a blockchain can be quite big, so we will search by hash
        sha = hashlib.sha256()
        sha.update(str(data).encode('utf-8'))
        hash = sha.hexdigest()

        current_node = self.tail
        while current_node is not None:
            if hash == current_node.hash:
                return True
            current_node = current_node.prev
        return False


# unit testing code
blockchain = BlockChain()
blockchain.add_block("This is the first block")
blockchain.add_block("This is the second block")
blockchain.add_block("This is the third block")
blockchain.add_block("This is the fourth block")
blockchain.add_block("This is the fifth block")


print("Pass" if blockchain.size() == 5 else "Fail")
print("Pass" if blockchain.search_block("This is the second block") else "Fail")
print("Pass" if not blockchain.search_block("This is the Second block") else "Fail")
print("Pass" if not blockchain.search_block("This is the tenth block") else "Fail")