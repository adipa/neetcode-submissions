class LRUCache:

    def __init__(self, capacity: int):
        # create cache hashmap
        self.cache = OrderedDict()
        # store capacity
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # if key dne return -1
        if key not in self.cache:
            return -1
        # if exists move to MRU and return val
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        # if key exists/dne update/add val
        self.cache[key] = value
        # move it to MRU
        self.cache.move_to_end(key)
        # if at capacity pop lru
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
# LRUCache lru = new LRUCache(2)
