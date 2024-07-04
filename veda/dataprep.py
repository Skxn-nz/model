import pandas as pd

# Load the generated data
data = pd.read_csv('sensor_data_with_solutions.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Select features (sensor values) and the target (solutions)
features = [col for col in data.columns if 'Exceeds_Threshold' not in col and 'Solution' not in col and 'Threshold' not in col]
target = [col for col in data.columns if 'Solution' in col]

# Combine all target columns into a single column
data['Solution'] = data[target].apply(lambda row: ' | '.join(row.values.astype(str)), axis=1)
data['Solution'] = data['Solution'].apply(lambda x: x if x != '' else 'No Action Required')

# Drop individual solution columns
data.drop(target, axis=1, inplace=True)

# Display the modified DataFrame
print(data.head())

# Select the final features and target
X = data[features]
y = data['Solution']
