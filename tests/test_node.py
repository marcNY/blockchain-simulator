import pytest
import simpy
from blockchain_simulator.node import Node


def test_node_initialization():
    env = simpy.Environment()
    state_data = []
    node = Node(env, 1, state_data)

    assert node.node_id == 1
    assert node.chain == []
    assert node.state_data == state_data
    assert isinstance(node.env, simpy.Environment)


def test_node_mining():
    env = simpy.Environment()
    state_data = []
    node = Node(env, 1, state_data)

    # Run simulation for a short time
    env.run(until=20)

    # Verify blocks were mined
    assert len(node.chain) > 0

    # Verify state data was recorded
    assert len(state_data) > 0

    # Check state data format
    first_state = state_data[0]
    assert "time" in first_state
    assert "node_id" in first_state
    assert "chain_length" in first_state
    assert first_state["node_id"] == 1
