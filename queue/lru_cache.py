import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.recently_used_freq = collections.defaultdict(int)
        self.lru_used_queue = collections.deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recently_used_freq[key] += 1
            self.lru_used_queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru_used_queue.append(key)
            self.recently_used_freq[key] += 1
        elif self.length < self.capacity:
            self.lru_used_queue.append(key)
            self.recently_used_freq[key] += 1
            self.cache[key] = value
            self.length += 1
        else:
            while self.length >= self.capacity:
                k = self.lru_used_queue.popleft()
                if k in self.recently_used_freq:
                    self.recently_used_freq[k] -= 1
                    if self.recently_used_freq[k] == 0:
                        del self.recently_used_freq[k]
                        del self.cache[k]
                        self.length -= 1
            self.lru_used_queue.append(key)
            self.recently_used_freq[key] += 1
            self.cache[key] = value
            self.length += 1


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

# -------------------------

# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

cache = LRUCache(2)
print(cache.get(2))
cache.put(2, 2)
print(cache.get(1))
cache.put(1, 1)
cache.put(1, 1.1)
print(cache.get(1))
print(cache.get(2))
