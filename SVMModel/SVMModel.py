from sklearn.svm import SVC
from GSModel import GSModel
from SVMSearchParameters import SVMSearchParameters
from SVMGridProperties import SVMGridProperties


class SVMModel(GSModel):
    def __init__(self):
        super().__init__()

    def init_name(self):
        self.name = 'SVM'
    
    def init_clf(self):
        self.clf = SVC()
    
    def init_grid(self):
        self.gs_grid = SVMGridProperties()
    
    def init_search_parameters(self):
        self.search_parameters = SVMSearchParameters()