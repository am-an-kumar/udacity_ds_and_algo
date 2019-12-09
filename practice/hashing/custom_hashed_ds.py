class Hashed_DS:
    def __init__(self):
        self.data = [None for _ in range(10)]
        self.num_elements = 0

    def hash_function(self, key):
        """
            Hash function for this hashed data structure
            :params: - 
                key - key of the value to store in the hashed data structure
            :output: -
                index - index for the key passed
            Time complexity - O(1)
        """
        return (key % len(self.data))

    def size(self):
        """
        Returns the size
            :params: - None
            :output: -
                size - size of the hashed data structure
        Time complexity - O(1)
        """
        return self.num_elements

    def is_empty(self):
        """
        Returns True/False based on if the hashed data structure is empty
            :params: - None
            :output: -
                is_empty - True/False based on whether the hashed data structure is empty
        Time complexity - O(1)
        """
        return self.num_elements == 0

    def get(self, key):
        """
        Retuns a value 
            :params: -
                key - key of the value to look up for and return
            :output: -
                value - value of the element looked up for and None if not found
        Time complexity - O(n), where n is the size of the hashed data structure. This is because if all the entries in the hashed data structure generated same value at time of insertion, then all the entries will be in a single bucket.
        """
        hash_value = self.hash_function(key)

        if not self.data[hash_value]:
            return None
        else:
            for value in self.data[hash_value]:
                if key == value["key"]:
                    return value
            return None

    def add(self, key, value):
        """
        Adds an element to the hashed data structure
            :params: - 
                key - key of the entry
                value - value of store
            :output: - None
        Time complexity - O(n), where n is the size of the hashed data structure. This is because if all the entries in the hashed data structure generated same value at time of insertion, then all the entries will be in a single bucket.
        """
        hash_value = self.hash_function(key)

        # there are no entries yet for this hash value, so we create a bucket
        if not self.data[hash_value]:
            self.data[hash_value] = []
            self.data[hash_value].append({
                "key": key,
                "value": value
            })
        else:
            self.data[hash_value].append({
                "key": key,
                "value": value
            })
        self.num_elements += 1

    def remove(self, key):
        """
        Removes an element from the hashed data structure
            :params: -
                key - key of the value to remove
            :output: -
                value - value of the element removed and None if nothing was found
        Time complexity - O(n), where n is the size of the hashed data structure. This is because if all the entries in the hashed data structure generated same value at time of insertion, then all the entries will be in a single bucket.
        """
        hash_value = self.hash_function(key)

        if not self.data[hash_value]:
            return None
        else:
            for index, value in enumerate(self.data[hash_value]):
                if key == value["key"]:
                    self.num_elements -= 1
                    return self.data[hash_value].pop(index)
            return None

    def __str__(self):
        """
        Returns the string representation of this hashed data structure
            :params: - None
            :output: -
                string_repr - string representation of the hashed data structure
        Time complexity - O(1)
        """
        return self.data

    def __repr__(self):
        """
        Returns the string representation of this hashed data structure
            :params: - None
            :output: -
                string_repr - string representation of the hashed data structure
        Time complexity - O(1)
        """
        return self.data


# This implementation will work with keys of type positive integer.
# Average time complexity of get(), remove() and add() - O(n/10), where n is the size of the hashed data structure, and 10 cause we are using 10 buckets. But the hash function is pretty primtive and does not guarantee even distribution, so it may happen that all entries end up in the same bucket.
# So, worst case complexity = O(n)
