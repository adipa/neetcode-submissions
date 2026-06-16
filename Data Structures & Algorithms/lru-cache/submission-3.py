class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # create cache hashmap
        self.cache = {}
        # store capacity
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


        

    def get(self, key: int) -> int:
        # if key dne return -1
        if key not in self.cache:
            return -1
        # if exists move to MRU and return val
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node

        
        

# class LRUCache:

#     def __init__(self, capacity: int):
#         # create cache hashmap
#         self.cache = OrderedDict()
#         # store capacity
#         self.capacity = capacity
        

#     def get(self, key: int) -> int:
#         # if key dne return -1
#         if key not in self.cache:
#             return -1
#         # if exists move to MRU and return val
#         self.cache.move_to_end(key)
#         return self.cache[key]


#     def put(self, key: int, value: int) -> None:
#         # if key exists/dne update/add val
#         self.cache[key] = value
#         # move it to MRU
#         self.cache.move_to_end(key)
#         # if greater than capacity pop lru
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

