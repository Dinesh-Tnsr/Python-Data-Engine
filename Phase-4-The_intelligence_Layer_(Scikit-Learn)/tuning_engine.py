import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Synthetic Data: App User Conversion (1=Premium, 0=Free)
data = {
    'Minutes': [10, 50, 15, 120, 5, 60, 20, 90, 8, 45, 12, 110, 18, 75, 6],
    'Clicks':  [2, 15, 5, 25, 1, 18, 6, 20, 2, 14, 4, 22, 7, 19, 1],
    'Days':    [1, 30, 2, 60, 1, 45, 5, 50, 1, 25, 3, 55, 4, 40, 1],
    'Premium': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print("--- Hyperparameter Tuning Engine Online ---")

y = df["Premium"]
X = df.drop("Premium", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators' : [10,50,100],
    'max_depth' : [None,2,5]
}

grid_search = GridSearchCV(estimator=rf,param_grid=param_grid,cv=5)

grid_search.fit(X_train,y_train)

predictions = grid_search.predict(X_test)

print(predictions,"\n")
print(grid_search.best_params_,"\n")
print(grid_search.best_score_)