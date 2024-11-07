import pytest
import numpy as np
from blockchain_simulator.mlmc import mlmc_simulation


def test_mlmc_simulation():
    # Test with minimal values for quick testing
    levels = 2
    samples_per_level = 2
    simulation_time = 10
    num_nodes = 2

    # Run MLMC simulation
    estimates = mlmc_simulation(levels, samples_per_level, simulation_time, num_nodes)

    # Verify number of estimates matches levels
    assert len(estimates) == levels

    # Verify estimates are numpy float64
    assert all(isinstance(est, np.float64) for est in estimates)

    # Verify estimates are positive
    assert all(est > 0 for est in estimates)

    # Verify estimates are reasonable (should be greater than 1 as each node mines at least 1 block)
    assert all(est >= 1.0 for est in estimates)


def test_mlmc_simulation_invalid_input():
    with pytest.raises(ValueError):
        mlmc_simulation(0, 10, 100, 5)  # Invalid levels

    with pytest.raises(ValueError):
        mlmc_simulation(3, 0, 100, 5)  # Invalid samples_per_level

    with pytest.raises(ValueError):
        mlmc_simulation(3, 10, 0, 5)  # Invalid simulation_time

    with pytest.raises(ValueError):
        mlmc_simulation(3, 10, 100, 0)  # Invalid num_nodes
