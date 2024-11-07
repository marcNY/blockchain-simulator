import numpy as np
import simpy


class Node:
    def __init__(self, env, node_id, state_data):
        self.env = env
        self.node_id = node_id
        self.chain = []
        self.state_data = state_data
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(np.random.exponential(10))
            block = f"Block_{len(self.chain)+1}_Node_{self.node_id}"
            self.chain.append(block)
            # Record state
            self.state_data.append(
                {
                    "time": self.env.now,
                    "node_id": self.node_id,
                    "chain_length": len(self.chain),
                }
            )
            print(f"Time {self.env.now}: Node {self.node_id} mined {block}")
