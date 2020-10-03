class LRU_Cache(object):

    def __init__(self, capacity):
        self.map = {}
        self.cache = LinkedList()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.map.get(key):
            return self.map.get(key).data[1]
        return -1

    def set(self, key, value):
        # if cache is at capacity remove oldest item
        if self.cache.count == self.capacity:
            tail = self.cache.remove_from_tail()
            self.map.pop(tail.data[0])
        # set new value
        node = Node((key, value))
        self.cache.prepend(node)
        self.map[key] = node


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def prepend(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.previous = None
            node.next.previous = node
            self.head = node
        self.count += 1

    def remove_from_tail(self):
        tmp = self.tail
        self.tail.previous.next = None
        self.tail = self.tail.previous
        self.count -= 1
        return tmp

    def move_to_head(self, node):
        # remove
        if node is self.tail:
            self.tail = node.previous
            node.previous.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        self.count -= 1
        self.prepend(node)


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


# Testing Cache Storage Backend
def test_linked_list():
    list = LinkedList()
    list.prepend(Node(1))
    list.prepend(Node(2))
    list.prepend(Node(3))
    list.prepend(Node(4))
    list.prepend(Node(5))
    list.remove_from_tail()
    list.move_to_head(list.head.next)
    list.move_to_head(list.tail)
    start = list.head
    end = list.tail

    while start:
        print(start.data)
        start = start.next

# test_linked_list()
# 2 4 5 3


# Testing Cache
cache = LRU_Cache(5)

cache.set(1, 'a')
cache.set(2, 'b')
cache.set(3, 'c')
cache.set(4, 'd')


print(cache.get(1))
# a
print(cache.get(2))
# b

cache.set(5, 'e')
cache.set(6, 'f')

print(cache.get(1))
# -1
