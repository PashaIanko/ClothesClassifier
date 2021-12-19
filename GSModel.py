from abc import ABC, abstractmethod

class GSModel(ABC):
    def __init__(self):
        self.name = None
        self.clf = None
        self.gs_grid = None
        self.search_parameters = None

        self.init_name()
        self.init_clf()
        self.init_grid()
        self.init_search_parameters()
    
    @abstractmethod
    def init_name(self):
        pass
    
    @abstractmethod
    def init_clf(self):
        pass
    
    @abstractmethod
    def init_grid(self):
        pass
    
    @abstractmethod
    def init_search_parameters(self):
        pass

    def get_grid(self):
        return self.gs_grid.get_grid()

    def get_search_parameters(self):
        return self.search_parameters.get_gs_params()

