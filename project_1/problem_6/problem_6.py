class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # all items in either list
    union = {}
    result = []
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        if not union.get(node1.value):
            union[node1.value] = 1
            result.append(node1.value)
        node1 = node1.next
    while node2:
        if not union.get(node2.value):
            union[node2.value] = 1
            result.append(node2.value)
        node2 = node2.next
    return list(set(result))


def intersection(llist_1, llist_2):
    intersection = {}
    result = []
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        intersection[node1.value] = 1
        node1 = node1.next
    while node2:
        if intersection.get(node2.value):
            result.append(node2.value)
        node2 = node2.next
    return list(set(result))


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]

print(intersection(linked_list_1, linked_list_2))
# [6, 4, 6, 21]


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]

print(intersection(linked_list_3, linked_list_4))
# []


# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))
# []

print(intersection(linked_list_5, linked_list_6))
# []

# Test case 3
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
linked_list_7.append(1)


print(union(linked_list_7, linked_list_8))
# [1]

print(intersection(linked_list_7, linked_list_8))
# []
