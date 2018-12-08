class Node(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, node):
        self.children.append(node)

    def add_metadata(self, data):
        self.metadata.append(data)

def generate_tree(numbers, idx):
    parent = Node()
    children = numbers[idx]
    metadata = numbers[idx+1]
    idx += 2
    for _ in range(children):
        child, idx = generate_tree(numbers, idx)
        parent.add_child(child)
    for _ in range(metadata):
        parent.add_metadata(numbers[idx])
        idx += 1
    return parent, idx

def print_tree(tree, level):
    print(' ' * 2 * level, tree.metadata)
    for child in tree.children:
        print_tree(child, level+1)

def sum_metadata_first(tree):
    checksum = 0
    checksum += sum(tree.metadata)
    for child in tree.children:
        checksum += sum_metadata_first(child)
    return checksum

def sum_metadata_second(tree):
    checksum = 0
    if len(tree.children) == 0:
        checksum += sum(tree.metadata)
    else:
        for idx in tree.metadata:
            if idx-1 < len(tree.children):
                checksum += sum_metadata_second(tree.children[idx-1])
    return checksum

def one(data):
    numbers = [int(x) for x in data[0].split()]
    tree, _ = generate_tree(numbers, 0)
    checksum = sum_metadata_first(tree)
    print(checksum)
    return checksum
    
def two(data):
    numbers = [int(x) for x in data[0].split()]
    tree, _ = generate_tree(numbers, 0)
    checksum = sum_metadata_second(tree)
    print(checksum)
    return checksum