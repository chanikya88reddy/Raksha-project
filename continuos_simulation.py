import joblib
import numpy as np
import pandas as pd
from time import sleep
from sensor_data import simulate_data
model = joblib.load('stress_detection_model.pkl')
data_file_path = 'simulated_data.csv'
def process_data():
    df = simulate_data(100)
    X = df[['heart_rate', 'hrv', 'pvr']]
    y_pred = model.predict(X)
    df['predictions'] = y_pred
    df.to_csv(data_file_path, index=False)
def main():
    print("Starting continuous simulation...")
    try:
        while True:
            process_data()
            sleep(60) 
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        print("Exiting the simulation script.")

if __name__ == "__main__":
    main()
