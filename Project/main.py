import matplotlib.pyplot as plt
import networkx as nx

def main():
    path_compsist = 'decks_network.gz'
    G = nx.read_edgelist(path_compsist, delimiter=',', comments=None)
    print(f"Original graph: {G}")
    G.remove_nodes_from([
        "Plains",
        "Island",
        "Swamp",
        "Mountain",
        "Forest"
    ])
    print(f"Without basic lands: {G}")

    # Draw graph.
    plt.figure()
    nx.draw_spring(G, with_labels=True, node_size=5)
    plt.show()

main()
