import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate sensor values and thresholds
def generate_sensor_data(sensor_name, mean, std, threshold, is_above_threshold=True):
    values = np.random.normal(mean, std, 100)
    if is_above_threshold:
        threshold_exceeded = values > threshold
    else:
        threshold_exceeded = values < threshold
    return values, threshold, threshold_exceeded

# Define sensors, their mean, std deviation, and thresholds
sensors = {
    'Engine Temperature': {'mean': 90, 'std': 10, 'threshold': 110, 'is_above_threshold': True},
    'Oil Quality': {'mean': 0.8, 'std': 0.1, 'threshold': 0.6, 'is_above_threshold': False},
    'Knock Sensor': {'mean': 0.5, 'std': 0.2, 'threshold': 1.0, 'is_above_threshold': True},
    'Brake Pad Wear': {'mean': 5, 'std': 2, 'threshold': 8, 'is_above_threshold': True},
    'Brake Temperature': {'mean': 70, 'std': 15, 'threshold': 120, 'is_above_threshold': True},
    'Brake Vibration': {'mean': 0.2, 'std': 0.05, 'threshold': 0.5, 'is_above_threshold': True},
    'Gear Torque': {'mean': 150, 'std': 20, 'threshold': 200, 'is_above_threshold': True},
    'Transmission Fluid Quality': {'mean': 0.7, 'std': 0.1, 'threshold': 0.5, 'is_above_threshold': False},
    'Transmission Speed': {'mean': 1000, 'std': 100, 'threshold': 1200, 'is_above_threshold': True},
    'Suspension Strain': {'mean': 30, 'std': 5, 'threshold': 40, 'is_above_threshold': True},
    'Shock Absorber Acceleration': {'mean': 0.3, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': True},
    'Tire Pressure': {'mean': 32, 'std': 2, 'threshold': 25, 'is_above_threshold': False},
    'Tire Tread Depth': {'mean': 8, 'std': 1, 'threshold': 3, 'is_above_threshold': False},
    'Battery Voltage': {'mean': 12.5, 'std': 0.5, 'threshold': 11.0, 'is_above_threshold': False},
    'Battery Current': {'mean': 50, 'std': 10, 'threshold': 30, 'is_above_threshold': False},
    'Battery Temperature': {'mean': 30, 'std': 5, 'threshold': 45, 'is_above_threshold': True},
    'Exhaust Pressure': {'mean': 15, 'std': 3, 'threshold': 20, 'is_above_threshold': True},
    'Exhaust Gas Quality': {'mean': 0.3, 'std': 0.1, 'threshold': 0.5, 'is_above_threshold': True},
    'Fuel Flow': {'mean': 60, 'std': 5, 'threshold': 50, 'is_above_threshold': False},
    'Fuel Pressure': {'mean': 40, 'std': 5, 'threshold': 30, 'is_above_threshold': False},
    'Fuel Quality': {'mean': 0.85, 'std': 0.1, 'threshold': 0.6, 'is_above_threshold': False},
    'Coolant Level': {'mean': 1.0, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': False},
    'Coolant Flow': {'mean': 20, 'std': 3, 'threshold': 15, 'is_above_threshold': False},
    'Coolant Temperature': {'mean': 85, 'std': 10, 'threshold': 100, 'is_above_threshold': True},
    'Steering Torque': {'mean': 10, 'std': 2, 'threshold': 15, 'is_above_threshold': True},
    'Steering Fluid Level': {'mean': 1.0, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': False},
    'Wire Current': {'mean': 5, 'std': 1, 'threshold': 8, 'is_above_threshold': True},
    'Wire Voltage': {'mean': 12, 'std': 1, 'threshold': 10, 'is_above_threshold': False},
    'Connector Temperature': {'mean': 30, 'std': 5, 'threshold': 50, 'is_above_threshold': True}
}

# Initialize a DataFrame to hold the sensor data
sensor_data = pd.DataFrame()

# Generate data for each sensor
for sensor, params in sensors.items():
    values, threshold, threshold_exceeded = generate_sensor_data(sensor, params['mean'], params['std'], params['threshold'], params['is_above_threshold'])
    sensor_data[sensor] = values
    sensor_data[sensor + '_Threshold'] = threshold
    sensor_data[sensor + '_Exceeds_Threshold'] = threshold_exceeded

# Display the first few rows of the DataFrame
print(sensor_data.head())

# Save the DataFrame to a CSV file
sensor_data.to_csv('sensor_data.csv', index=False)
