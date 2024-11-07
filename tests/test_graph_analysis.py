import pytest
import igraph
from blockchain_simulator.graph_analysis import analyze_graph


def test_analyze_graph():
    # Test with small number of nodes
    num_nodes = 3
    min_cut = analyze_graph(num_nodes)

    # Verify min_cut is returned and is positive
    assert isinstance(min_cut, float)
    assert min_cut > 0

    # For a fully connected graph with n nodes, min_cut should be n-1
    assert min_cut == num_nodes - 1


def test_analyze_graph_invalid_input():
    with pytest.raises(ValueError):
        analyze_graph(0)  # Invalid number of nodes

    with pytest.raises(ValueError):
        analyze_graph(-1)  # Negative number of nodes


def test_analyze_graph_visualization(tmp_path):
    # Test if visualization is created
    num_nodes = 4
    output_file = tmp_path / "test_graph.png"

    min_cut = analyze_graph(num_nodes, output_file=str(output_file))

    # Verify output file was created
    assert output_file.exists()

    # Verify file is not empty
    assert output_file.stat().st_size > 0
