import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the generated data
data = pd.read_csv('sensor_data_with_solutions.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Define features and target columns
features = [col for col in data.columns if 'Exceeds_Threshold' not in col and 'Solution' not in col and 'Threshold' not in col]
solution_cols = [col for col in data.columns if 'Solution' in col]

# Combine all solution columns into a single column
data['Solution'] = data[solution_cols].apply(lambda row: ' | '.join(row.dropna().values.astype(str)), axis=1)
data['Solution'] = data['Solution'].apply(lambda x: x if x != '' else 'No Action Required')

# Drop individual solution columns
data.drop(solution_cols, axis=1, inplace=True)

# Display the modified DataFrame
print(data.head())

# Select the final features and target
X = data[features]
y = data['Solution']

# Check for any NaN values in the features or target
print("Checking for NaN values in features or target:")
print(X.isna().sum())
print(y.isna().sum())

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Define multiple new sensor readings that need actions
test_cases = pd.DataFrame([
    {
        'Engine Temperature': 115,
        'Oil Quality': 0.55,
        'Knock Sensor': 1.2,
        'Brake Pad Wear': 9,
        'Brake Temperature': 130,
        'Brake Vibration': 0.6,
        'Gear Torque': 210,
        'Transmission Fluid Quality': 0.45,
        'Transmission Speed': 1300,
        'Suspension Strain': 45,
        'Shock Absorber Acceleration': 0.8,
        'Tire Pressure': 22,
        'Tire Tread Depth': 2,
        'Battery Voltage': 10.5,
        'Battery Current': 25,
        'Battery Temperature': 50,
        'Exhaust Pressure': 25,
        'Exhaust Gas Quality': 0.6,
        'Fuel Flow': 45,
        'Fuel Pressure': 25,
        'Fuel Quality': 0.5,
        'Coolant Level': 0.6,
        'Coolant Flow': 12,
        'Coolant Temperature': 105,
        'Steering Torque': 18,
        'Steering Fluid Level': 0.5,
        'Wire Current': 9,
        'Wire Voltage': 9.5,
        'Connector Temperature': 55
    },
    {
        'Engine Temperature': 90,
        'Oil Quality': 0.65,
        'Knock Sensor': 0.3,
        'Brake Pad Wear': 7,
        'Brake Temperature': 75,
        'Brake Vibration': 0.2,
        'Gear Torque': 180,
        'Transmission Fluid Quality': 0.85,
        'Transmission Speed': 1100,
        'Suspension Strain': 30,
        'Shock Absorber Acceleration': 0.3,
        'Tire Pressure': 32,
        'Tire Tread Depth': 6,
        'Battery Voltage': 12.5,
        'Battery Current': 50,
        'Battery Temperature': 40,
        'Exhaust Pressure': 15,
        'Exhaust Gas Quality': 0.3,
        'Fuel Flow': 55,
        'Fuel Pressure': 35,
        'Fuel Quality': 0.7,
        'Coolant Level': 0.85,
        'Coolant Flow': 20,
        'Coolant Temperature': 85,
        'Steering Torque': 14,
        'Steering Fluid Level': 0.8,
        'Wire Current': 5,
        'Wire Voltage': 12,
        'Connector Temperature': 35
    },
    {
        'Engine Temperature': 80,
        'Oil Quality': 0.4,
        'Knock Sensor': 0.8,
        'Brake Pad Wear': 8,
        'Brake Temperature': 110,
        'Brake Vibration': 0.5,
        'Gear Torque': 190,
        'Transmission Fluid Quality': 0.5,
        'Transmission Speed': 1200,
        'Suspension Strain': 40,
        'Shock Absorber Acceleration': 0.7,
        'Tire Pressure': 28,
        'Tire Tread Depth': 4,
        'Battery Voltage': 11,
        'Battery Current': 35,
        'Battery Temperature': 45,
        'Exhaust Pressure': 20,
        'Exhaust Gas Quality': 0.4,
        'Fuel Flow': 50,
        'Fuel Pressure': 30,
        'Fuel Quality': 0.6,
        'Coolant Level': 0.7,
        'Coolant Flow': 15,
        'Coolant Temperature': 95,
        'Steering Torque': 16,
        'Steering Fluid Level': 0.6,
        'Wire Current': 7,
        'Wire Voltage': 10.5,
        'Connector Temperature': 45
    }
])

# Predict solutions for the new sensor readings
predicted_solutions = model.predict(test_cases)
print("Predicted Solutions:", predicted_solutions)

# Add the predicted solutions to the test cases DataFrame for better visualization
test_cases['Predicted Solution'] = predicted_solutions

# Save the test cases with predictions to a new CSV file
test_cases.to_csv('test_cases_with_predictions.csv', index=False)
print("Test cases with predictions have been saved to 'test_cases_with_predictions.csv'.")
