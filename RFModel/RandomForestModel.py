from sklearn.ensemble import RandomForestClassifier
from GSModel import *
from GridProperties import *
from RFGridProperties import *
from RFSearchParameters import *


class RandomForestModel(GSModel):
    def __init__(self):
        super().__init__()

    def init_name(self):
        self.name = 'RandomForest'
    
    def init_clf(self):
        self.clf = RandomForestClassifier()
    
    def init_grid(self):
        self.gs_grid = RFGridProperties()
    
    def init_search_parameters(self):
        self.search_parameters = RFSearchParameters()