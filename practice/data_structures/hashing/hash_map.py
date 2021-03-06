from single_linked_list import SinglyLinkedList


class HashMap:
    def __init__(self, initial_size=10):
        self.num_entries = 0
        # prime number used for hash code generation
        self.p = 37
        self.bucket_array = [None for _ in range(initial_size)]
        self.load_factor = 0.7

    def compression_function(self, hashcode):
        """ 
        Maps hash_code to bucket index
            :params: - 
                hashcode - hashcode to map to bucket index
            :output: -
                bucket_index - bucket index for input hashcode
        Time complexity - O(1)
        """
        return hashcode % len(self.bucket_array)

    def hash_function(self, key):
        """
        Returns the hash code for input string
            :params: -
                key - string to find the hash code of
            :output: -
                hash_value - hash value / hash code of the input string
        Time complexity - O(k), where k = len(str(key))
        """
        key = str(key)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p
        return hash_code

    def get_bucket_index(self, key):
        """
        Returns the bucket index for a key
            :params: -
                key - key to find bucket index for
            :output: -
                bucket_index - bucket index for input key
        Time complexity - O(k), where k = len(str(key))
        """
        return self.compression_function(self.hash_function(key))

    def rehash(self):
        """ 
        Rehashes the hash map to decrease the load factor
            :params: - None
            :output: - None
        Time complexity - O(2 * current_bucket_size) + O(n) = O(n)
        """
        self.num_entries = 0
        old_bucket_array = self.bucket_array
        self.bucket_array = [None for _ in range(2 * len(old_bucket_array))]

        for bucket_entry in old_bucket_array:
            current_node = bucket_entry.head if bucket_entry else None
            while current_node is not None:
                key = current_node.value["key"]
                value = current_node.value["value"]
                self.put(key, value)
                current_node = current_node.next

    def delete(self, key):
        """
        Deletes an entry from hashmap
            :params: - 
                key - key corresponding entry of which is to be deleted
            :output: -
                value - value removed from hashmap and None if no entry with the input key is found
        Time complexity - O(n/b), n = number of entries in hashmap, b = number of buckets in bucket_array
        Worst case complexity = O(n), if all entries end up in the same bucket
        """
        bucket_index = self.get_bucket_index(key)
        if self.bucket_array[bucket_index] is None:
            return None

        else:
            head = self.bucket_array[bucket_index].head
            current_node = head
            prev_node = None
            while current_node is not None:
                if current_node.value["key"] == key:
                    # the first node needs to be removed
                    if prev_node is None:
                        value = current_node.value["value"]
                        self.bucket_array[bucket_index].head = current_node.next
                        self.num_entries -= 1
                        return value

                    # some node other than first node needs to be removed
                    else:
                        value = current_node.value["value"]
                        prev_node.next = current_node.next
                        self.num_entries -= 1
                        return value

                prev_node = current_node
                current_node = current_node.next

            # entry was not found
            return None

    def put(self, key, value):
        """
        Adds an entry into hashmap, if already present, updates the value
            :params: -
                key - key of the value to insert
                value - value 
            :output: - None
        Time complexity - O(1)
        Worst case time complexity - O(n), if put causes rehashing
        """
        bucket_index = self.get_bucket_index(key)

        # bucket array index is empty, so key is not present already
        if self.bucket_array[bucket_index] is None:
            self.bucket_array[bucket_index] = SinglyLinkedList()
            self.bucket_array[bucket_index].prepend({
                "key": key,
                "value": value
            })

        else:

            # searching to find the entry, if found, we will update the value instead of creating a new entry
            head = self.bucket_array[bucket_index].head
            current_node = head
            while current_node is not None:
                if current_node.value["key"] == key:
                    current_node.value["value"] = value
                    return
                current_node = current_node.next

            self.bucket_array[bucket_index].prepend({
                "key": key,
                "value": value
            })

        self.num_entries += 1

        # check for load factor
        if (self.num_entries / len(self.bucket_array)) > self.load_factor:
            self.rehash()

    def get(self, key):
        """
        Returns the value associated with the passed key
            :params: -
                key - key of the value to get
            :output: -
                value - value associated with the key or None if no such entry exists
        Time complexity - O(n/b)
        Worst case time complexity - O(n)
        """
        bucket_index = self.get_bucket_index(key)
        if self.bucket_array[bucket_index] is None:
            return None
        else:
            head = self.bucket_array[bucket_index].head
            current_node = head
            while current_node is not None:
                if current_node.value["key"] == key:
                    return current_node.value
                current_node = current_node.next

    def size(self):
        """
        Returns the size of hashmap
            :params: - None
            :output: -
                size - size of the hashmap
        Time complexity - O(1)
        """
        return self.num_entries


    def __str__(self):
        """
        Returns the string representation of hashmap
            :params: - None
            :output: -
                string_repr - string representation of hashmap
        Time complexity - O(1)
        """
        return "bucket: {}\nsize: {}\nload factor: {}\nPrime number used for hashing: {}".format(self.bucket_array, self.num_entries, self.load_factor, self.p)
    
    def __repr__(self):
        """
        Returns the string representation of hashmap
            :params: - None
            :output: -
                string_repr - string representation of hashmap
        Time complexity - O(1)
        """
        return "bucket: {}\nsize: {}\nload factor: {}\nPrime number used for hashing: {}".format(self.bucket_array, self.num_entries, self.load_factor, self.p)
