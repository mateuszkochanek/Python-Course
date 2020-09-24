import random

class Node(object):
    val = 0
    nodes = []
    def __init__(self):
        self.val = random.randint(0, 100)
        number_of_nodes = random.randint(0, 4)
        self.nodes = [None for x in range(0,number_of_nodes)]

def generate_tree(n,is_main_now):
    node = Node()
    if n>0:
        if is_main_now:
            while not node.nodes:
                node = Node()
        if is_main_now == 1:
            node.nodes[0] = generate_tree(n-1,1)
            for i, x in enumerate(node.nodes[1:], 1):
                node.nodes[i] = generate_tree(n - 1, random.randint(0, 1))
        else:
            for i, x in enumerate(node.nodes, 0):
                node.nodes[i] = generate_tree(n - 1, random.randint(0, 1))
    return node

def DFS(root):
    yield root.val
    for x in root.nodes:
        if x != None:
            yield from DFS(x)

def BFS(root,n):
    for i in range(1, n + 2):
        yield from print_level(root, i)

def print_level(root, level):
    if level == 1:
        yield root.val
    else:
        for x in root.nodes:
            if x != None:
                yield from print_level(x, level-1)

n = input("Wprowadz n:")
tree = generate_tree(int(n),1)
for x in DFS(tree):
    print(x)
print("--------------------------")
for k in BFS(tree,int(n)):
    print(k);