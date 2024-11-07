# Blockchain Simulator

An advanced blockchain network simulator for analyzing state space and network topology, employing Multi-Level Monte Carlo simulations and graph analysis techniques.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installing Poetry](#installing-poetry)
    - [Installing Cairo](#installing-cairo)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
    - [Running the Simulation](#running-the-simulation)
    - [Analyzing Results](#analyzing-results)
    - [Visualization](#visualization)
- [Demonstrations](#demonstrations)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The Blockchain Simulator is designed to simulate blockchain networks, analyze their state space and topology, and apply advanced simulation techniques to identify vulnerabilities and critical points. It provides insights into blockchain performance and potential points of failure, making it a valuable tool for researchers and developers in the blockchain space.

## Features

- **State Space Analysis**: Identify and analyze discontinuities and critical points within the blockchain state space.
- **Graph Topology Analysis**: Use igraph to analyze network topology and identify vulnerabilities using techniques like mincut.
- **Advanced Simulation Techniques**: Apply Multi-Level Monte Carlo simulations for accelerated and accurate results.
- **Efficient Simulation Workflows**: Implemented using Python libraries and optimized for performance.
- **Visualization**: Generate plots to visualize simulation results and analyses.
- **Extensibility**: Modular codebase for easy extension and customization.

## Installation

### Prerequisites

- Python 3.8+
- Poetry: Python dependency management tool.
- Cairo Graphics Library: Required by pycairo, a dependency of python-igraph.

### Installing Poetry

Install Poetry using pip:

```sh
pip install poetry
```

Or install via the official installer:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

For more details, visit the [Poetry installation guide](https://python-poetry.org/docs/#installation).

### Installing Cairo

#### On macOS

Using Homebrew:

```sh
brew install cairo
```

#### On Ubuntu/Debian

```sh
sudo apt-get install libcairo2-dev
```

#### On Windows

Download and install the Cairo Graphics Library for Windows.

### Clone the Repository

```sh
git clone https://github.com/yourusername/Blockchain-Simulator.git
cd Blockchain-Simulator
```

### Install Dependencies

Using Poetry:

```sh
poetry install
```

This command will create a virtual environment and install all dependencies specified in `pyproject.toml`.

If you prefer using pip, you can install dependencies from `requirements.txt`:

```sh
pip install -r requirements.txt
```

Note: The `requirements.txt` file can be generated using `poetry export`.

## Usage

### Running the Simulation

Activate the Poetry shell to use the virtual environment:

```sh
poetry shell
```

Run the main simulation script:

```sh
python src/simulation.py
```

This will execute the blockchain simulation using the default parameters. You can adjust simulation settings by modifying the `simulation.py` script or by adding command-line arguments (if implemented).

### Analyzing Results

After running the simulation, the results are stored in the `data/` directory, typically in the `state_data.csv` file. To perform graph topology analysis and identify vulnerabilities:

```sh
python src/graph_analysis.py
```

This script will analyze the network graph and output metrics such as the minimum cut value.

### Visualization

To visualize the simulation results, including chain lengths over time and discontinuities:

```sh
python src/visualization.py
```

This will generate plots and graphs saved in the `plots/` directory or display them directly, depending on the implementation.

## Demonstrations

An interactive Jupyter notebook is provided for demonstrations and tutorials.

1. Install Jupyter if you haven’t already:

        ```sh
        pip install jupyterlab
        ```

2. Launch Jupyter Lab:

        ```sh
        jupyter lab
        ```

3. Open `notebooks/demonstration.ipynb` and follow the step-by-step instructions.

The notebook includes code snippets, explanations, and visualizations to help you understand how to use and extend the simulator.

## Project Structure

```
Blockchain-Simulator/
├── LICENSE
├── README.md
├── pyproject.toml
├── poetry.lock
├── src/
│   ├── __init__.py
│   ├── simulation.py
│   ├── node.py
│   ├── mlmc.py
│   ├── graph_analysis.py
│   └── visualization.py
├── data/
│   └── state_data.csv
├── notebooks/
│   └── demonstration.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_simulation.py
│   ├── test_node.py
│   ├── test_mlmc.py
│   └── test_graph_analysis.py
├── requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- SimPy: For process-based discrete-event simulation.
- igraph: For complex network analysis.
- Matplotlib: For plotting and visualization.
- NumPy & Pandas: For numerical computations and data manipulation.
