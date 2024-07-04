import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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

# Encode target labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Check for any NaN values in the features or target
print("Checking for NaN values in features or target:")
print(X.isna().sum())
print(y.isna().sum())

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(len(np.unique(y)), activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save the model
model.save('sensor_solution_model')

# Save the label encoder classes
np.save('label_classes.npy', label_encoder.classes_)
