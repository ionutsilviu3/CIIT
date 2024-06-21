import pandas as pd
import random
import datetime

# Function to generate serials
def generate_serials(start_day, end_day, num_serials):
    
    serials = []
    current_day = start_day
    serial_id = 1
    
    # Loop over the specified timeframe
    while current_day <= end_day and len(serials) < num_serials:
        for hour in range(24):
            for minute in range(0, 60, random.choice([4, 5, 6])):  # Generate serials at random intervals
                # Generate random hour and minute
                rand_hour = str(hour).zfill(2)
                rand_minute = str(minute).zfill(2)
                
                # Generate serial for each serial type
                serial_types = [('FP', 1), ('IV', 2), ('BS', 3)]  # Fuel Pump, Power Inverter, Brake Sensor
                for serial_type, serial_type_id in serial_types:
                    serial = f"{serial_type}{serial_type_id}D{current_day.strftime('%y%m%d')}T{rand_hour}{rand_minute}I{serial_id}"
                    serials.append((serial, serial_type_id, datetime.datetime.strptime(f"{current_day.strftime('%y%m%d')} {rand_hour}{rand_minute}", '%y%m%d %H%M')))
                    serial_id += 1
                    
                    if len(serials) >= num_serials:
                        break
                
                if len(serials) >= num_serials:
                    break
            
            if len(serials) >= num_serials:
                break
        
        current_day += datetime.timedelta(days=1)
    
    return serials

# Function to generate process events, results, limits, and parameters
def generate_data(serial_df):
    
        # Predefined parameters and limits
    parameters_data = [
        {'name': 'Voltage', 'unit_of_measurement': 'V'},
        {'name': 'Current Draw', 'unit_of_measurement': 'A'},
        {'name': 'Resistance', 'unit_of_measurement': 'ohm'},
        {'name': 'Motor RPM', 'unit_of_measurement': 'RPM'},
        {'name': 'Pressure', 'unit_of_measurement': 'psi'},
        {'name': 'Flow Rate', 'unit_of_measurement': 'liters per hour'},
        {'name': 'Efficiency', 'unit_of_measurement': '%'},
        {'name': 'Sound Levels', 'unit_of_measurement': 'dB(A)'},
        {'name': 'Harmonic Distortion', 'unit_of_measurement': '%'},
        {'name': 'Operating Temperature', 'unit_of_measurement': '°C'}
    ]

    limits_data = [
        {'parameter_id': 1, 'serial_type_id': 1, 'lower_limit': 11.4, 'upper_limit': 12.6, 'created_at': '2019-02-21 00:00:00'},
        {'parameter_id': 2, 'serial_type_id': 1, 'lower_limit': 4.75, 'upper_limit': 15.25, 'created_at': '2019-03-12 00:00:00'},
        {'parameter_id': 3, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 0.95, 'created_at': '2019-06-24 00:00:00'},
        {'parameter_id': 4, 'serial_type_id': 1, 'lower_limit': 1900, 'upper_limit': 6100, 'created_at': '2019-08-24 00:00:00'},
        {'parameter_id': 5, 'serial_type_id': 1, 'lower_limit': 28.5, 'upper_limit': 81.5, 'created_at': '2019-08-24 00:00:00'},
        {'parameter_id': 6, 'serial_type_id': 1, 'lower_limit': 95, 'upper_limit': 205, 'created_at': '2019-09-28 00:00:00'},
        {'parameter_id': 7, 'serial_type_id': 1, 'lower_limit': 69.5, 'upper_limit': 100, 'created_at': '2019-10-13 00:00:00'},
        {'parameter_id': 8, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 66.5, 'created_at': '2019-11-04 00:00:00'},
        {'parameter_id': 9, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 4.75, 'created_at': '2019-11-18 00:00:00'},
        {'parameter_id': 10, 'serial_type_id': 1, 'lower_limit': -42, 'upper_limit': 122, 'created_at': '2019-12-07 00:00:00'}
    ]
    process_events = []
    results = []

    # Loop through each row in the serial DataFrame
    for index, row in serial_df.iterrows():
        serial_id = row['id']
        serial_type_id = row['serial_type_id']
        created_at = row['created_at']

        # Generate process events for each station
        for station_id, station_name in [(1, "S100"), (2, "S120"), (3, "S150"), (4, "S200")]:
            # Define process event
            process_event = {
                "event_type_id": 2,
                "serial_id": serial_id,
                "station_id": station_id,
                "start_time": created_at - datetime.timedelta(minutes=3),  # Start time 3 minutes before serial creation
                "end_time": created_at
            }
            process_events.append(process_event)

            # Generate results for each parameter
            for parameter_id, parameter_data in enumerate(parameters_data, start=1):
                lower_limit = next(limit['lower_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                upper_limit = next(limit['upper_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                
                # Generate result
                value = random.uniform(lower_limit, upper_limit)
                result = {
                    "event_id": len(process_events),  # Use the index of the process event
                    "parameter_id": parameter_id,
                    "value": value,
                    "created_at": created_at
                }
                results.append(result)

    return process_events, results