from GridSearchParameters import *

class RFSearchParameters(GridSearchParameters):
    def __init__(self):
        super().__init__()

    def init_gs_params(self):
        self.gs_params = {
            'verbose': 0,
            'cv': 5,
            'n_jobs': -1
        }
