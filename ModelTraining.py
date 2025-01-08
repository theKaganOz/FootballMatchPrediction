import pandas as pd
import numpy as np

path    = r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\football_match_dataset_processed.csv"
dataset = pd.read_csv(path)

dataset.dropna(inplace=True)

all_features = list(dataset.columns)
referee_variables   = [feature for feature in all_features if "Referee_" in feature]
home_team_variables = [feature for feature in all_features if "HomeTeam_" in feature]
away_team_variables = [feature for feature in all_features if "AwayTeam_" in feature]
goals = ["FullTimeHomeTeamGoals", "FullTimeAwayTeamGoals"]
target_features = ["HomeTeamWin", "AwayTeamWin", "Draw"]
other_predictors = all_features[7:19] 

#other_predictors.append("Date")

from itertools import chain
predictors = list(chain(referee_variables,
                        home_team_variables,
                        away_team_variables,
                        other_predictors))

X, y = dataset[predictors], dataset[goals + target_features]
y["2.5U"] = ((y["FullTimeHomeTeamGoals"] + y["FullTimeAwayTeamGoals"]) > 2.5).astype(float)
y["1.5U"] = ((y["FullTimeHomeTeamGoals"] + y["FullTimeAwayTeamGoals"]) > 1.5).astype(float)

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import GridSearchCV 


parameter_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10, ],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'criterion': ['gini', 'entropy']
    }


base_model_clf = RandomForestClassifier()
models_for_clf = {}
for var in list(y.columns[-5:]):
    grid_search = GridSearchCV(estimator=base_model_clf, 
                               param_grid=parameter_grid).fit(X, y[var])
    models_for_clf[var] = grid_search.best_estimator_
    
base_model_reg = RandomForestRegressor()
models_for_reg = {}
for var in list(y.columns[:2]):
    grid_search = GridSearchCV(estimator=base_model_reg, 
                               param_grid=parameter_grid).fit(X, y[var])
    models_for_reg[var] = grid_search.best_estimator_
