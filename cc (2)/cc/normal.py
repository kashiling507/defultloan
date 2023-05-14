import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('credit_card.csv')

# Convert categorical variables into numerical variables using one-hot encoding
df = pd.get_dummies(df, columns=['SEX', 'EDUCATION', 'MARRIAGE'])

# Split the data into training and testing sets
X = df.drop('default.payment.next.month', axis=1)
y = df['default.payment.next.month']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the LightGBM models
model1 = lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=31, max_depth=5, learning_rate=0.1, n_estimators=100)
model2 = lgb.LGBMClassifier(boosting_type='dart', num_leaves=31, max_depth=5, learning_rate=0.1, n_estimators=100)
model3 = lgb.LGBMClassifier(boosting_type='goss', num_leaves=31, max_depth=5, learning_rate=0.1, n_estimators=100)

# Create the ensemble
ensemble = VotingClassifier(estimators=[('model1', model1), ('model2', model2), ('model3', model3)], voting='hard')

# Train the ensemble
ensemble.fit(X_train, y_train)

# Predict using the ensemble
y_pred = ensemble.predict(X_test)

# Output the results in a CSV file
output = pd.DataFrame({'ID': X_test.index, 'Default': y_pred})
output.to_csv('credit_card_predictions.csv', index=False)
# Save the trained model
import joblib
joblib.dump(ensemble, 'trained_model.joblib')

