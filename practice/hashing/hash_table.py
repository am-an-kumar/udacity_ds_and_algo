class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
        self.num_elements = 0

    def store(self, string):
        """
        Stores a string in the hash table
            :params: -
                string - string to store in hash table
            :output: - None
        Time complexity - O(n), with append(), the complexity would have been O(1), but we are looking up to see if the string already exists in the hash table, and since the strings are not sorted, it will take linear time. 
        Average complexity - O(n/10000)
        Worst case complexity - O(n), if all entries end up in the same hash bucket, i.e., entries are like "SAlsa", "SAsha" and so on, i.e., the first 2 characters are the same, cause that dictates the hash value
        """
        hash_value = self.calculate_hash_value(string)

        # if a list is not created at that hash table index yet
        if self.table[hash_value] is None:
            self.table[hash_value] = []
            self.table[hash_value].append(string)
        else:
            # looking up to see if the string already exists, not adding it again in that case
            if string in self.table[hash_value]:
                return
            self.table[hash_value].append(string)
        self.num_elements += 1

    def lookup(self, string):
        """
        Returns hash value if string is found, else -1
            :params: -
                string - string to do lookup for
            :output: -
                hash_value - hash value if string is present, else -1
        Average case time complexity - O(n/10000)
        Worst case time complexity - O(n)
        """
        hash_value = self.calculate_hash_value(string)
        # no list at that index of hash table
        if self.table[hash_value] is None:
            return -1
        else:
            if string in self.table[hash_value]:
                return hash_value
            else:
                return -1

    def calculate_hash_value(self, string):
        """
        Returns the hash value for a string
            :params: -
                string - string to calculate the hash for
            :output: -
                hash_value - hash value of the string
        Time complexity - O(1)
        """
        return ord(string[0]) * 100 + ord(string[1])

    def size(self):
        """
        Returns the size or number of entries in hash table
            :params: - None
            :output: -
                size - number of entries in the hash table
        Time complexity - O(1)
        """
        return self.num_elements


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
