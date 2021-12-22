from GridProperties import GridProperties

class SVMGridProperties(GridProperties):
    def __init__(self):
        super().__init__()

    def init_grid(self):
        self.grid_dict = {
            'C': [0.1, 1, 10],
            'kernel': ['rbf', 'linear']
        }