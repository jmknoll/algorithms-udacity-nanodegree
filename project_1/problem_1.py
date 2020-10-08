from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache.keys():
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        if self.capacity <= 0:
            return None
        # if cache is at capacity remove oldest item
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return True

        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
        return True


# Test Cache 1
print("test case 1")
cache = LRU_Cache(5)

cache.set(1, "a")
cache.set(2, "b")
cache.set(3, "c")
cache.set(4, "d")


print(cache.get(1))
# a
print(cache.get(2))
# b

cache.set(5, "e")
cache.set(6, "f")

print(cache.get(1))
# -1

# Test Cache 2
print("test case 2")
cache = LRU_Cache(1)

cache.set(1, "a")
cache.set(4, "d")


print(cache.get(1))
# -1
print(cache.get(4))
# d

# Test Cache 3
print("test case 3")
cache = LRU_Cache(0)

cache.set(1, "a")

print(cache.get(1))
# -1


our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get(4)  # Expected Value = 4
our_cache.get(1)  # Expected Value = -1
our_cache.set(2, 4)
our_cache.get(2)  # Expected Value = 4
our_cache.set(5, 5)
our_cache.get(3)  # Expected Value = -1
our_cache.get(5)  # Expected Value = 5
our_cache.set(2, 6)
our_cache.get(2)  # Expected Value = 6
our_cache.set(6, 6)
our_cache.get(4)  # Expected Value = -1
our_cache.get(6)  # Expected Value = 6
our_cache.set(5, 10)
our_cache.set(7, 7)
