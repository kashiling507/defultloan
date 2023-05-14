import joblib
from sklearn.ensemble import VotingClassifier

# Load the trained model
model = joblib.load('trained_model.joblib')

# Print the feature names
print(model.named_estimators_['lgbm'].feature_name_)
