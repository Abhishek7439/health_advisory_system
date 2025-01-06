import time
import random
import pandas as pd

def generate_health_data():
    while True:
        data = {
            'timestamp': pd.Timestamp.now(),
            'heart_rate': random.randint(60, 120),  # Random heart rate
            'steps': random.randint(0, 50),        # Random steps
            'calories': random.uniform(0.1, 2.0), # Random calories burned
        }
        print(data)
        pd.DataFrame([data]).to_csv('health_data.csv', mode='a', header=False, index=False)
        time.sleep(1)  # Generate new data every second

generate_health_data()
