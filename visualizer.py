import networkx as nx
import matplotlib.pyplot as plt


def visualize_priority_queue(elements):

    G = nx.DiGraph()

    # Build heap structure
    for i in range(len(elements)):

        G.add_node(i)

        left = 2*i + 1
        right = 2*i + 2

        if left < len(elements):
            G.add_edge(i, left)

        if right < len(elements):
            G.add_edge(i, right)

    # Calculate tree layout
    pos = {}

    levels = {}

    for i in range(len(elements)):
        level = int((i + 1).bit_length() - 1)
        levels.setdefault(level, []).append(i)

    vertical_gap = 2

    for level, nodes in levels.items():
        horizontal_gap = 6 / (len(nodes) + 1)

        for j, node in enumerate(nodes):
            x = (j + 1) * horizontal_gap
            y = -level * vertical_gap
            pos[node] = (x, y)

    labels = {i: elements[i] for i in range(len(elements))}

    plt.figure(figsize=(8,5))
    nx.draw(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=14,
        arrows=False
    )

    return plt