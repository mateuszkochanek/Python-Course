import random
def generate_tree(n,is_main_now):
    children = [random.randint(0, 100)]
    if n > 0:
        n -= 1
        my_random = generate_rand_node()
        is_main = random.randint(0, 1)
        if is_main_now == 1:
            while my_random == None:
                my_random = generate_rand_node()
        children.append(my_random)
        if children[0] != None:
            children += [generate_tree(n, is_main)]
            children += [generate_tree(n, 1 - is_main)]
    else:
        children.append(None)
    return children

def generate_rand_node():
    node = [random.randint(0, 100)]
    number_of_nodes = random.randint(0, 5)
    if number_of_nodes == 0:
        return None
    else:
        while number_of_nodes > 0:
            node.append(None)
            number_of_nodes-=1
        return node

def DFS(tree):
    yield tree[0]
    for x in tree:
        if x != None and isinstance(x,list):
            yield from DFS(x)


def BFS(tree,n):
    for i in range(1, n + 2):
        yield from print_level(tree, i)

def print_level(tree, level):
    if level == 1:
        yield tree[0]
    else:
        for x in tree[1:]:
            if x != None:
                yield from print_level(x, level-1)

n = input("Wprowadz n:")
tree = generate_tree(int(n),1)
print(tree)
for k in DFS(tree):
    print(k);
print("--------------------------")
for k in BFS(tree,int(n)):
    print(k);