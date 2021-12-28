from labels.label_interface import Label

class Label1(Label):
    def __init__(self, num_nodes, num_edges, mask, label_name):
        super(Label1, self).__init__(num_nodes, num_edges, mask, label_name)
        self._generate_regions()
        self._generate_patterns()
        # self.A = self._make_symmetric(self.A) * self.mask / 2
        
    def _generate_regions(self):
        super()._generate_regions()

if __name__ == '__main__':
    pass