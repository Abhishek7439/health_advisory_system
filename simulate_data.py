import time
import random
import pandas as pd

def generate_health_data():
    while True:
        data = {
            'timestamp': pd.Timestamp.now(),
            'heart_rate': random.randint(60, 120),  # Random heart rate between 60-120
            'steps': random.randint(0, 50),  # Random number of steps (0-50)
            'calories': random.uniform(0.1, 2.0),  # Random calories burned (0.1-2.0)
        }
        print(data)
        # Append the data to the CSV file (without the header every time)
        pd.DataFrame([data]).to_csv('health_data.csv', mode='a', header=False, index=False)
        time.sleep(1)  # Simulate new data every 1 second

# Start generating data
generate_health_data()
