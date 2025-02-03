import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F5"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def change_color(step, base_color="#1296F5"):
    r, g, b = (
        int(base_color[1:3], 16),
        int(base_color[3:5], 16),
        int(base_color[5:7], 16),
    )

    r_light = min(255, r + step * 10)
    g_light = min(255, g + step * 10)
    b_light = min(255, b + step * 10)

    return f"#{hex(r_light)[2:].zfill(2)}{hex(g_light)[2:].zfill(2)}{hex(b_light)[2:].zfill(2)}"


def bfs_traversal(root):
    queue = [root]
    step = 0
    while queue:
        step += 1
        node = queue.pop(0)
        if not node:
            continue

        node.color = change_color(step)

        queue.append(node.left)
        queue.append(node.right)
    draw_tree(root)


def dfs_traversal(root):
    stack = [root]
    step = 0
    while stack:
        step += 1
        node = stack.pop()
        if not node:
            continue

        node.color = change_color(step)

        stack.append(node.right)
        stack.append(node.left)
    draw_tree(root)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Обхід у ширину (BFS):")
bfs_traversal(root)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Обхід у глибину (DFS):")
dfs_traversal(root)
