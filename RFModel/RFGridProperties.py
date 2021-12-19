from GridProperties import *

class RFGridProperties(GridProperties):
    def __init__(self):
        super().__init__()

    def init_grid(self):
        self.grid_dict = {
            'criterion': ['entropy'],
            'max_depth': [3, 5]
        }