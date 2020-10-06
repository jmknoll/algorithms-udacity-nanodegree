import sys
import heapq


def huffman_encoding(data):
    if data is None or data is "":
        return ("0", None)

    # calculate frequencies
    frequencies = calculate_frequencies(data)
    # build priority queue
    pq = create_priority_queue(frequencies)
    # build huffman tree
    tree = build_huffman_tree(pq)

    # create encoding map and encode string
    encoding = create_huffman_encoding(tree)
    encoded_string = ""
    for letter in data:
        encoded_string += encoding[letter]
    return encoded_string, tree


def calculate_frequencies(str):

    freq = {}
    for char in str:
        if freq.get(char):
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def create_priority_queue(frequencies):
    h = []

    for key in frequencies.keys():
        # some strange naming in here to invert k,v of frequencies map
        frequency = frequencies[key]
        node = create_node(frequency, key)
        heapq.heappush(h, (frequency, id(node), node))
    return h


def build_huffman_tree(pq):
    while len(pq) > 1:
        node1 = heapq.heappop(pq)[2]
        node2 = heapq.heappop(pq)[2]
        node3 = {
            "frequency": node1["frequency"] + node2["frequency"],
            "left": node1,
            "right": node2,
        }
        heapq.heappush(pq, (node3["frequency"], id(node3), node3))
    return heapq.heappop(pq)[2]


def create_node(frequency, value=None, left=None, right=None):
    return {"frequency": frequency, "value": value, "left": left, "right": right}


def create_huffman_encoding(node, prefix="", encoding={}):
    if node["left"]:
        create_huffman_encoding(node["left"], prefix + "0", encoding)
    if node["right"]:
        create_huffman_encoding(node["right"], prefix + "1", encoding)
    if node["left"] is None and node["right"] is None:
        encoding[node["value"]] = prefix
        return encoding
    return encoding


def huffman_decoding(data, root, d_string=""):
    if data or root is None:
        return ""
    d_string = ""
    node = root
    for num in data:
        if node == None:
            return
        if num == "0":
            node = node["left"]
        if num == "1":
            node = node["right"]
        if node["left"] is None and node["right"] is None:
            d_string += node["value"]
            node = root
    return d_string


# Test Case 1
print("==== Test Case 1 =====")
a_great_sentence = "The bird is the word"

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print(
    "The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))
    )
)
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))


# Test Case 2
print("==== Test Case 2 =====")
test_sentence_2 = "aaaaa aaa"

print("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_2)))
print("The content of the data is: {}\n".format(test_sentence_2))

encoded_data, tree = huffman_encoding(test_sentence_2)

print(
    "The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))
    )
)
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))


# Test Case 3
print("==== Test Case 3 =====")
test_sentence_3 = ""

print("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_3)))
print("The content of the data is: {}\n".format(test_sentence_3))

encoded_data, tree = huffman_encoding(test_sentence_3)

print(
    "The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))
    )
)
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
