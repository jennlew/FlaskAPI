class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

