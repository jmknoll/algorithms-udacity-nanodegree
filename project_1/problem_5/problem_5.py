import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode("utf-8"))
        sha.update(str(self.data).encode("utf-8"))
        sha.update(str(self.previous_hash).encode("utf-8"))
        return sha.hexdigest()


class Blockchain:
    def __init__(self, data):
        timestamp = datetime.datetime.now()
        self.root = Block(timestamp, data, None)
        self.head = self.root
        self.length = 1

    def append(self, data):
        timestamp = datetime.datetime.now()
        block = Block(timestamp, data, self.head)
        self.head = block
        self.length += 1


# Test Case 1
bc = Blockchain(1)
bc.append(2)
bc.append(3)

node = bc.head
while node:
    print(node.hash)
    node = node.previous_hash

# Test Case 2
bc2 = Blockchain(1)
i = 0
while i < 1000:
    bc2.append(i)
    i += 1


node2 = bc2.head
while node2:
    print(node2.hash)
    node2 = node2.previous_hash


# Test Case 3
bc3 = Blockchain(None)

node3 = bc3.head
while node3:
    print(node3.hash)
    node3 = node3.previous_hash
