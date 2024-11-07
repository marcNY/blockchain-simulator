# src/visualization.py

import matplotlib.pyplot as plt
import pandas as pd
from igraph import Graph, plot as igraph_plot


def plot_chain_length(
    state_df: pd.DataFrame, num_nodes: int, discontinuities: pd.DataFrame = None
):
    """
    Plot chain lengths over time for each node.

    Parameters:
    - state_df (pd.DataFrame): DataFrame containing state data.
    - num_nodes (int): Number of nodes in the network.
    - discontinuities (pd.DataFrame, optional): DataFrame containing discontinuity data.
    """
    plt.figure(figsize=(12, 8))
    for node_id in range(num_nodes):
        node_data = state_df[state_df["node_id"] == node_id]
        plt.step(
            node_data["time"],
            node_data["chain_length"],
            where="post",
            label=f"Node {node_id}",
        )
        if discontinuities is not None:
            node_discontinuities = discontinuities[
                discontinuities["node_id"] == node_id
            ]
            for dt in node_discontinuities["time"]:
                plt.axvline(x=dt, color="r", linestyle="--", alpha=0.5)
    plt.xlabel("Time")
    plt.ylabel("Chain Length")
    plt.title("Chain Length Over Time with Discontinuities")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/chain_length_over_time.png")
    plt.show()


def plot_mlmc_estimates(estimates: list):
    """
    Plot MLMC estimates over levels.

    Parameters:
    - estimates (list): List of MLMC estimates per level.
    """
    levels = list(range(1, len(estimates) + 1))
    plt.figure(figsize=(8, 6))
    plt.plot(levels, estimates, marker="o", linestyle="-", color="b")
    plt.xlabel("MLMC Level")
    plt.ylabel("Estimate of Average Chain Length")
    plt.title("MLMC Estimates over Levels")
    plt.xticks(levels)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/mlmc_estimates.png")
    plt.show()


def visualize_graph(num_nodes: int):
    """
    Visualize the network graph.

    Parameters:
    - num_nodes (int): Number of nodes in the network.
    """
    g = Graph.Full(num_nodes)
    layout = g.layout("circle")
    igraph_plot(
        g,
        layout=layout,
        vertex_label=[f"Node {i}" for i in range(num_nodes)],
        vertex_color="lightblue",
        vertex_size=30,
        edge_color="gray",
        bbox=(300, 300),
        margin=20,
        target="plots/network_graph.png",
    )
    print("Network graph saved to plots/network_graph.png")


if __name__ == "__main__":
    # Example usage
    state_df = pd.read_csv("data/state_data.csv")
    # Assume discontinuities have been identified and saved to 'data/discontinuities.csv'
    try:
        discontinuities = pd.read_csv("data/discontinuities.csv")
    except FileNotFoundError:
        discontinuities = None
    num_nodes = state_df["node_id"].nunique()
    plot_chain_length(state_df, num_nodes, discontinuities)
    # Assume MLMC estimates are saved or computed elsewhere
    # Example: estimates = [10, 10.5, 10.25]
    # plot_mlmc_estimates(estimates)
    visualize_graph(num_nodes)
