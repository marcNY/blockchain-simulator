# src/simulation.py

import simpy
import numpy as np
import pandas as pd
from blockchain_simulator.node import Node


def run_simulation(simulation_time: int, num_nodes: int) -> pd.DataFrame:
    """
    Run the blockchain simulation.

    Parameters:
    - simulation_time (int): Duration to run the simulation.
    - num_nodes (int): Number of blockchain nodes.

    Returns:
    - state_df (pd.DataFrame): DataFrame containing state data collected during the simulation.
    """
    env = simpy.Environment()
    state_data = []
    nodes = [Node(env, i, state_data) for i in range(num_nodes)]
    env.run(until=simulation_time)
    state_df = pd.DataFrame(state_data)
    state_df.to_csv("data/state_data.csv", index=False)
    print(f"Simulation completed. Data saved to 'data/state_data.csv'.")
    return state_df


def main():
    simulation_time = 100  # Define simulation time
    num_nodes = 5  # Define number of nodes
    run_simulation(simulation_time, num_nodes)


if __name__ == "__main__":
    main()
