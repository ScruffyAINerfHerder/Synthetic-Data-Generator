import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Constants
BASE_VOLTAGE = 240
UPPER_LIMIT = 252
LOWER_LIMIT = 228
ANOMALY_PERCENTAGE = 0.05  # 5% of the data points are anomalies
NUM_DAYS = 365
HOURS_PER_DAY = 24
NUM_METERS = 5
NUM_CIRCUITS = 3

# Generate datetime range
date_range = pd.date_range(start='2023-01-01', periods=NUM_DAYS*HOURS_PER_DAY, freq='H')

# Function to generate synthetic meter data
def generate_meter_data(meter_id, circuit_id):
    np.random.seed(meter_id + circuit_id)  # Ensure reproducibility
    voltage_readings = np.random.normal(loc=BASE_VOLTAGE, scale=1, size=len(date_range))
    current_readings = np.random.normal(loc=10, scale=1, size=len(date_range))
    power_readings = voltage_readings * current_readings / 1000  # Simplified power calculation
    reactive_power_readings = power_readings * np.random.uniform(0.3, 0.6, len(date_range))
    apparent_power_readings = np.sqrt(power_readings**2 + reactive_power_readings**2)
    power_factor_readings = power_readings / apparent_power_readings
    frequency_readings = np.full(len(date_range), 60)  # Constant frequency
    temperature_readings = np.random.uniform(15, 35, len(date_range))  # Simulated temperature data
    status_flags = np.zeros(len(date_range), dtype=int)
    anomaly_indicator = np.zeros(len(date_range), dtype=int)

    # Introduce anomalies
    num_anomalies = int(len(date_range) * ANOMALY_PERCENTAGE)
    anomaly_indices = random.sample(range(len(date_range)), num_anomalies)

    for idx in anomaly_indices:
        if random.choice([True, False]):
            # Upper limit violation
            voltage_readings[idx] = np.random.uniform(UPPER_LIMIT, UPPER_LIMIT + 5)
        else:
            # Lower limit violation
            voltage_readings[idx] = np.random.uniform(LOWER_LIMIT - 5, LOWER_LIMIT)
        status_flags[idx] = 1
        anomaly_indicator[idx] = 1

    # Create DataFrame for the meter
    data = {
        'Timestamp': date_range,
        'Meter ID': meter_id,
        'Circuit ID': circuit_id,
        'Voltage (V)': voltage_readings,
        'Current (A)': current_readings,
        'Power (kW)': power_readings,
        'Reactive Power (kVAR)': reactive_power_readings,
        'Apparent Power (kVA)': apparent_power_readings,
        'Power Factor': power_factor_readings,
        'Frequency (Hz)': frequency_readings,
        'Temperature (°C)': temperature_readings,
        'Status Flags': status_flags,
        'Anomaly Indicator': anomaly_indicator
    }
    return pd.DataFrame(data)

# Generate data for all meters
all_data = []
for circuit_id in range(1, NUM_CIRCUITS + 1):
    for meter_id in range(1, NUM_METERS + 1):
        meter_data = generate_meter_data(meter_id, circuit_id)
        all_data.append(meter_data)

# Concatenate all data into a single DataFrame
df_all_data = pd.concat(all_data, ignore_index=True)

# Save to CSV
df_all_data.to_csv('synthetic_ami_voltage_data.csv', index=False)

# Display the first few rows of the generated data
print(df_all_data.head())
