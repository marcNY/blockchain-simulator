import pytest
import pandas as pd
from blockchain_simulator.simulation import run_simulation


def test_run_simulation():
    # Test with small values for quick testing
    simulation_time = 10
    num_nodes = 3

    # Run simulation
    result_df = run_simulation(simulation_time, num_nodes)

    # Verify the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)

    # Check DataFrame has required columns
    required_columns = ["time", "node_id", "chain_length"]
    assert all(col in result_df.columns for col in required_columns)

    # Verify node_ids are within expected range
    assert result_df["node_id"].min() >= 0
    assert result_df["node_id"].max() < num_nodes

    # Verify chain lengths are positive
    assert (result_df["chain_length"] > 0).all()

    # Verify timestamps are within simulation time
    assert result_df["time"].min() >= 0
    assert result_df["time"].max() <= simulation_time
