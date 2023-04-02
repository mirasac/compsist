import matplotlib.pyplot as plt
import networkx as nx

def main():
    path_compsist = 'decks_network.gz'
    G = nx.read_edgelist(path_compsist, delimiter=',', comments=None)
    print(f"Original graph: {G}")
    basic_lands = [
        "Plains",
        "Island",
        "Swamp",
        "Mountain",
        "Forest"
    ]
    G.remove_nodes_from(basic_lands)
    print(f"Without basic lands: {G}")

    # Draw graph.
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=False, node_size=5)
    plt.show()
    nx.draw(G, pos=pos, with_labels=True, node_size=5)
    plt.show()

main()
