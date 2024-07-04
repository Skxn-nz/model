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

# Define sensors, their mean, std deviation, thresholds, and solutions
sensors = {
    'Engine Temperature': {'mean': 90, 'std': 10, 'threshold': 110, 'is_above_threshold': True, 'solution': 'Check coolant levels and radiator function.'},
    'Oil Quality': {'mean': 0.8, 'std': 0.1, 'threshold': 0.6, 'is_above_threshold': False, 'solution': 'Change engine oil.'},
    'Knock Sensor': {'mean': 0.5, 'std': 0.2, 'threshold': 1.0, 'is_above_threshold': True, 'solution': 'Inspect engine timing and fuel quality.'},
    'Brake Pad Wear': {'mean': 5, 'std': 2, 'threshold': 8, 'is_above_threshold': True, 'solution': 'Replace brake pads.'},
    'Brake Temperature': {'mean': 70, 'std': 15, 'threshold': 120, 'is_above_threshold': True, 'solution': 'Inspect brake system and avoid prolonged braking.'},
    'Brake Vibration': {'mean': 0.2, 'std': 0.05, 'threshold': 0.5, 'is_above_threshold': True, 'solution': 'Inspect and replace brake rotors.'},
    'Gear Torque': {'mean': 150, 'std': 20, 'threshold': 200, 'is_above_threshold': True, 'solution': 'Check transmission fluid and gear alignment.'},
    'Transmission Fluid Quality': {'mean': 0.7, 'std': 0.1, 'threshold': 0.5, 'is_above_threshold': False, 'solution': 'Replace transmission fluid.'},
    'Transmission Speed': {'mean': 1000, 'std': 100, 'threshold': 1200, 'is_above_threshold': True, 'solution': 'Inspect transmission for slippage.'},
    'Suspension Strain': {'mean': 30, 'std': 5, 'threshold': 40, 'is_above_threshold': True, 'solution': 'Inspect suspension components for wear.'},
    'Shock Absorber Acceleration': {'mean': 0.3, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': True, 'solution': 'Replace shock absorbers.'},
    'Tire Pressure': {'mean': 32, 'std': 2, 'threshold': 25, 'is_above_threshold': False, 'solution': 'Inflate tires to proper pressure.'},
    'Tire Tread Depth': {'mean': 8, 'std': 1, 'threshold': 3, 'is_above_threshold': False, 'solution': 'Replace tires.'},
    'Battery Voltage': {'mean': 12.5, 'std': 0.5, 'threshold': 11.0, 'is_above_threshold': False, 'solution': 'Charge or replace the battery.'},
    'Battery Current': {'mean': 50, 'std': 10, 'threshold': 30, 'is_above_threshold': False, 'solution': 'Check for electrical issues and recharge battery.'},
    'Battery Temperature': {'mean': 30, 'std': 5, 'threshold': 45, 'is_above_threshold': True, 'solution': 'Inspect cooling system and battery.'},
    'Exhaust Pressure': {'mean': 15, 'std': 3, 'threshold': 20, 'is_above_threshold': True, 'solution': 'Check for exhaust blockages and leaks.'},
    'Exhaust Gas Quality': {'mean': 0.3, 'std': 0.1, 'threshold': 0.5, 'is_above_threshold': True, 'solution': 'Inspect catalytic converter and engine performance.'},
    'Fuel Flow': {'mean': 60, 'std': 5, 'threshold': 50, 'is_above_threshold': False, 'solution': 'Inspect fuel pump and filter.'},
    'Fuel Pressure': {'mean': 40, 'std': 5, 'threshold': 30, 'is_above_threshold': False, 'solution': 'Check fuel pump and pressure regulator.'},
    'Fuel Quality': {'mean': 0.85, 'std': 0.1, 'threshold': 0.6, 'is_above_threshold': False, 'solution': 'Refuel with high-quality fuel.'},
    'Coolant Level': {'mean': 1.0, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': False, 'solution': 'Refill coolant.'},
    'Coolant Flow': {'mean': 20, 'std': 3, 'threshold': 15, 'is_above_threshold': False, 'solution': 'Check water pump and coolant system.'},
    'Coolant Temperature': {'mean': 85, 'std': 10, 'threshold': 100, 'is_above_threshold': True, 'solution': 'Inspect radiator and cooling system.'},
    'Steering Torque': {'mean': 10, 'std': 2, 'threshold': 15, 'is_above_threshold': True, 'solution': 'Inspect steering components and fluid levels.'},
    'Steering Fluid Level': {'mean': 1.0, 'std': 0.1, 'threshold': 0.7, 'is_above_threshold': False, 'solution': 'Refill steering fluid.'},
    'Wire Current': {'mean': 5, 'std': 1, 'threshold': 8, 'is_above_threshold': True, 'solution': 'Inspect wiring for overloads and shorts.'},
    'Wire Voltage': {'mean': 12, 'std': 1, 'threshold': 10, 'is_above_threshold': False, 'solution': 'Check for voltage drops and power supply issues.'},
    'Connector Temperature': {'mean': 30, 'std': 5, 'threshold': 50, 'is_above_threshold': True, 'solution': 'Inspect connectors for corrosion and poor connections.'}
}

# Initialize a DataFrame to hold the sensor data
sensor_data = pd.DataFrame()

# Generate data for each sensor
for sensor, params in sensors.items():
    values, threshold, threshold_exceeded = generate_sensor_data(sensor, params['mean'], params['std'], params['threshold'], params['is_above_threshold'])
    solutions = np.where(threshold_exceeded, params['solution'], '')
    sensor_data[sensor] = values
    sensor_data[sensor + '_Threshold'] = threshold
    sensor_data[sensor + '_Exceeds_Threshold'] = threshold_exceeded
    sensor_data[sensor + '_Solution'] = solutions

# Display the first few rows of the DataFrame
print(sensor_data.head())

# Save the DataFrame to a CSV file
sensor_data.to_csv('sensor_data_with_solutions.csv', index=False)
