from labels.label_interface import Label

class Label1(Label):
    def __init__(self, num_nodes, num_edges, mask, label_name):
        super(Label1, self).__init__(num_nodes, num_edges, mask, label_name)
        self._generate_regions()
        self._generate_patterns()
        self.A = self._make_symmetric(self.A) * self.mask
        
    def _generate_regions(self):
        super()._generate_regions()
        self.connections = {
            'strong': self.connections['strong'] + [('r1', 'r3'), ('r1', 'r4'), ('r1', 'r5')],
            'weak': [('r2', 'r3'), ('r1', 'r2'), ('r2', 'r4'), ('r2', 'r5')],
            'weakest': [('r3', 'r4'), ('r3', 'r5'), ('r4', 'r5')]
        }

if __name__ == '__main__':
    pass