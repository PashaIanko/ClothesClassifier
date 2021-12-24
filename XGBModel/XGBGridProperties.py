from GridProperties import GridProperties

class XGBGridProperties(GridProperties):
    def __init__(self):
        super().__init__()

    def init_grid(self):
        self.grid_dict = {
            'learning_rate': [0.1, 0.01],
            'n_estimators': [100, 200, 400],
            'subsample': [1.0, 0.85],
            'max_depth': [3, 5],
            'random_state': [123],
            'max_features': [0.8]            
        }