from GridSearchParameters import *

class RFSearchParameters(GridSearchParameters):
    def __init__(self):
        super().__init__()

    def update_gs_params(self):
        # No update, keep same search parameters as in parent
        self.gs_params.update({})  
