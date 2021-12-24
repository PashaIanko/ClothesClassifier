from sklearn.ensemble import GradientBoostingClassifier
from GSModel import GSModel
from XGBSearchParameters import XGBSearchParameters
from XGBGridProperties import XGBGridProperties


class XGBModel(GSModel):
    def __init__(self):
        super().__init__()

    def init_name(self):
        self.name = 'GradientBoosting'
    
    def init_clf(self):
        self.clf = GradientBoostingClassifier()
    
    def init_grid(self):
        self.gs_grid = XGBGridProperties()
    
    def init_search_parameters(self):
        self.search_parameters = XGBSearchParameters()