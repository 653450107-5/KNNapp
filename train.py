import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('hypertension_data.csv')

# Update column names to match CSV
data.columns = ['Age', 'Weight (kg)', 'Height (cm)', 'Systolic_BP', 'Diastolic_BP', 'Heart_Rate', 'Hypertension']

# Prepare features and target variable
X = data[['Age', 'Weight (kg)', 'Height (cm)', 'Systolic_BP', 'Diastolic_BP', 'Heart_Rate']].values
y = data['Hypertension'].values

# Split data into training and testing sets (adjust test_size as needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=32)

# Create a decision tree classifier
kNN_model = KNeighborsClassifier(n_neighbors=15)

# Train the decision tree on the training set
kNN_model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = kNN_model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)

filename = 'model.sav'
pickle.dump(kNN_model, open(filename, 'wb'))

print(f"Accuracy: {accuracy:.4f}")