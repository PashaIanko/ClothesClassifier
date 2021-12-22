from sklearn.tree import DecisionTreeClassifier
from GSModel import GSModel
from DTSearchParameters import DTSearchParameters
from DTGridProperties import DTGridProperties


class DTModel(GSModel):
    def __init__(self):
        super().__init__()

    def init_name(self):
        self.name = 'DecisionTree'
    
    def init_clf(self):
        self.clf = DecisionTreeClassifier()
    
    def init_grid(self):
        self.gs_grid = DTGridProperties()
    
    def init_search_parameters(self):
        self.search_parameters = DTSearchParameters()