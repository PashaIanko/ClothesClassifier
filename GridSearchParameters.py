from abc import ABC, abstractmethod

class GridSearchParameters(ABC):
    def __init__(self):
        self.gs_params = {
            'verbose': 1,
            'cv': 5,
            'n_jobs': -1
        }
        self.update_gs_params()
    
    @abstractmethod
    def update_gs_params(self):
        pass
    
    def get_gs_params(self):
        return self.gs_params
