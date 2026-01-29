1from collections import OrderedDict
2
3class LRUCache:
4
5    def __init__(self, capacity: int):
6        self.capacity = capacity
7        self.cache = OrderedDict()
8
9    def get(self, key: int) -> int:
10        if key not in self.cache:
11            return -1
12
13        # mark as recently used
14        self.cache.move_to_end(key)
15        return self.cache[key]
16
17    def put(self, key: int, value: int) -> None:
18        if key in self.cache:
19            # update and move to recent
20            self.cache.move_to_end(key)
21
22        self.cache[key] = value
23
24        # remove LRU if over capacity
25        if len(self.cache) > self.capacity:
26            self.cache.popitem(last=False)