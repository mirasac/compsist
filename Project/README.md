Some little things maybe useful for the project.

I try to write a script that translates Pauperformance decks files to a file that can be read by networkx to do some network analysis.
The file is in the branch `decks_network` in the `pauperformance-bot` repo.

A first test file with the network of decks is the one in archive `decks_network.gz`.

Ideas:
1. Undirected graph, each different card in MTG is a node, links are created when the property "both cards are in the same deck" is satisfied. Only mainboard is considered.
2. Bipartite weighted directed graph with decks and cards as nodes, edges point to deck nodes following the rule "the card is in the deck", where the weights are the number of copies in the deck.
