import joblib
import numpy as np
import pandas as pd
from time import sleep
from sensor_data import simulate_data

# Load the trained model
model = joblib.load('stress_detection_model.pkl')

# Path to save simulated data
data_file_path = 'simulated_data.csv'

def process_data():
    df = simulate_data(100)  # Generate new data
    X = df[['heart_rate', 'hrv', 'pvr']]
    
    # Predict using the loaded model
    y_pred = model.predict(X)
    
    # Save the data and predictions
    df['predictions'] = y_pred
    df.to_csv(data_file_path, index=False)  # Save data for the alert system to read

def main():
    print("Starting continuous simulation...")
    try:
        while True:
            process_data()  # Process data and save to file
            sleep(60)  # Adjust the frequency as needed
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        print("Exiting the simulation script.")

if __name__ == "__main__":
    main()
