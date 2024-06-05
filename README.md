Explanation
Constants
BASE_VOLTAGE: The base voltage value around which normal readings are generated.
UPPER_LIMIT and LOWER_LIMIT: Voltage thresholds for detecting anomalies.
ANOMALY_PERCENTAGE: Percentage of data points that are anomalies.
NUM_DAYS, HOURS_PER_DAY, NUM_METERS, NUM_CIRCUITS: Parameters defining the duration of data, number of meters, and circuits.
Functions
generate_meter_data(meter_id, circuit_id): Generates synthetic data for a specific meter and circuit, including introducing anomalies.
Data Generation and Storage
The script iterates over all meters and circuits, generates the data, and concatenates it into a single DataFrame which is then saved to a CSV file.

Sample Output
The first few rows of the generated data are displayed using df_all_data.head().

Resulting Data
The data is saved in synthetic_ami_voltage_data.csv and includes the following columns:

Timestamp: Date and time of the reading.
Meter ID: Identifier for the meter.
Circuit ID: Identifier for the circuit.
Voltage (V), Current (A), Power (kW), Reactive Power (kVAR), Apparent Power (kVA), Power Factor, Frequency (Hz), Temperature (°C): Various readings.
Status Flags: Indicates if there was a status issue.
Anomaly Indicator: Marks if the reading was an anomaly.
Feel free to modify the script as needed for your specific use case.
