# src/mlmc.py

import numpy as np
import pandas as pd
from .simulation import run_simulation


def mlmc_simulation(
    levels: int, samples_per_level: int, simulation_time: int, num_nodes: int
) -> list:
    """
    Perform Multi-Level Monte Carlo (MLMC) simulation.

    Parameters:
    - levels (int): Number of MLMC levels.
    - samples_per_level (int): Number of samples per level.
    - simulation_time (int): Duration to run each simulation.
    - num_nodes (int): Number of nodes in the blockchain network.

    Returns:
    - estimates (list): List of MLMC estimates per level.
    """
    estimates = []
    for level in range(levels):
        samples = samples_per_level * (2**level)
        results = []
        print(f"Starting Level {level} with {samples} samples...")
        for sample in range(samples):
            state_df = run_simulation(simulation_time, num_nodes)
            avg_chain_length = state_df["chain_length"].mean()
            results.append(avg_chain_length)
            if (sample + 1) % max(1, samples // 10) == 0:
                print(f"  Progress: {((sample + 1) / samples) * 100:.1f}%")
        estimate = np.mean(results)
        estimates.append(estimate)
        print(f"Level {level} completed. Estimate: {estimate}\n")
    return estimates


if __name__ == "__main__":
    levels = 3
    samples_per_level = 10
    simulation_time = 100
    num_nodes = 5
    estimates = mlmc_simulation(levels, samples_per_level, simulation_time, num_nodes)
    print(f"MLMC Estimates: {estimates}")
