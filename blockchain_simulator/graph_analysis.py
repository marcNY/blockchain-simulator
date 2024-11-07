import igraph
from igraph import Graph
import matplotlib.pyplot as plt


def analyze_graph(num_nodes):
    g = Graph.Full(num_nodes)
    min_cut_value = g.mincut().value
    print(f"The minimum cut of the network graph is {min_cut_value}")

    layout = g.layout("circle")
    fig, ax = plt.subplots()
    igraph.plot(g, layout=layout, target=ax)
    plt.show()


if __name__ == "__main__":
    analyze_graph(num_nodes=5)
