from GridProperties import GridProperties

class DTGridProperties(GridProperties):
    def __init__(self):
        super().__init__()

    def init_grid(self):
        self.grid_dict = {
            'max_depth': [2, 4, 6, 8]
        }