import numpy as np
import random
import json

class Label:
    def __init__(self, num_nodes, num_edges, mask, label_name):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.name = label_name
        self.mask = mask
        self.A = np.zeros((num_nodes, num_nodes))

    def _make_symmetric(self, matrix):
        return (matrix + matrix.T)

    def _generate_regions(self):
        nn = self.num_nodes
        self.regions = {
            'r1': range(0, int(nn*0.3)),
            'r2': range(int(nn*0.3), int(nn*0.7)),
            'r3': range(int(nn*0.85), nn),
            'r4': range(int(nn*0.3), int(nn*0.4)),
            'r5': range(int(nn*0.7), int(nn*0.85))
        }
        self.weights = {
            'strong': (0.8, 1),
            'weak': (0.15, 0.5),
            'weakest': (0, 0.15)
        }
        self.connections = {
            'strong': [('r1', 'r1'), ('r2', 'r2'), ('r3', 'r3'), ('r4', 'r4'), ('r5', 'r5')],
            'weak': [],
            'weakest': []
        }

    def _fill_region_with_values(self, r1, r2, values):
        for i, row in enumerate(r1):
            for j, col in enumerate(r2):
                self.A[row, col] += values[i+j]
        self.A /= np.max(self.A)

    def _generate_patterns(self):
        for conn, regss in self.connections.items():
            ws = self.weights[conn]
            for regs in regss:
                num_values = len(self.regions[regs[0]]) * len(self.regions[regs[1]])
                values = list([(random.uniform(ws[0], ws[1])) for _ in range(num_values)])
                self._fill_region_with_values(self.regions[regs[0]], self.regions[regs[1]], values)

    def _generate_edge_index_coo_format(self):
        self.edge_index_coo = np.array(self.mask.nonzero())

    def _generate_edge_attr(self):
        edge_index_T = np.transpose(self.edge_index_coo)
        edge_attr = []
        for edge in edge_index_T:
            feat = self.A[edge[0], edge[1]]
            edge_attr.append(feat)
        self.edge_attr = np.array(edge_attr)

    def to_json(self, path):
        self._generate_edge_index_coo_format()
        self._generate_edge_attr()
        data = {
            'num_nodes': self.num_nodes,
            'edge_attr': json.dumps(self.edge_attr.tolist()),
            'edge_index': json.dumps(self.edge_index_coo.tolist())
        }
        json.dump(data, open(path/f'{self.name}.json', 'w'))


if __name__ == '__main__':
    pass