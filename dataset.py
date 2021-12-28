from labels import *
import numpy as np
from pathlib import Path

class Dataset:
    def __init__(self, num_per_label: dict, num_nodes: int, num_edges: int, mask, dir: str):
        self.num_per_label = num_per_label
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.dir = dir
        self.mask = mask
        self._generate_dataset()

    def _generate_dataset(self):
        for LabelClass, (name, num) in self.num_per_label.items():
            Path(self.dir, name).mkdir(exist_ok=True)
            for i in range(num):
                graph = LabelClass(self.num_nodes, self.num_edges, self.mask, f'{i+1}')
                graph.to_json(Path(self.dir, name))


def make_symmetric(matrix):
    return (matrix + matrix.T)

def generate_mask(num_nodes, num_edges):
    edges_ratio = num_edges / (num_nodes * (num_nodes - 1) // 2)

    mask = np.random.uniform(0, 1, num_nodes**2).reshape(num_nodes, num_nodes)
    symm_mask = make_symmetric(mask) / 2
    mask = np.where((symm_mask < edges_ratio), 1, 0)
    np.fill_diagonal(mask, 0)
    return mask


if __name__ == '__main__':
    train = {
        Label1: ('label1', 5),
        Label2: ('label2', 5),
        Label3: ('label3', 5),
        Label4: ('label4', 5),
    }
    val = {
        Label1: ('label1', 2),
        Label2: ('label2', 2),
        Label3: ('label3', 2),
        Label4: ('label4', 2),
    }
    test = {
        Label1: ('label1', 1),
        Label2: ('label2', 1),
        Label3: ('label3', 1),
        Label4: ('label4', 1),
    }
    num_nodes = 5
    num_edges = num_nodes * (num_nodes - 1) // 2
    mask = generate_mask(num_nodes, num_edges)
    print(mask)
    train_dataset = Dataset(train, num_nodes, num_edges, mask, './dataset_inner_conn/train')
    val_dataset = Dataset(val, num_nodes, num_edges, mask, './dataset_inner_conn/valid')
    test_dataset = Dataset(test, num_nodes, num_edges, mask, './dataset_inner_conn/test')