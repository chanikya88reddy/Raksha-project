import pandas as pd
import os
from time import sleep
from speech_recognition_test import recognize_speech, detect_trigger_words

# Path to the simulated data file
data_file_path = 'simulated_data.csv'

def check_stress():
    if os.path.exists(data_file_path):
        df = pd.read_csv(data_file_path)
        latest_data = df.iloc[-1]  # Get the latest data entry
        predicted_stress = latest_data['predictions']
        return predicted_stress
    return None

def main():
    print("Starting alert system...")
    try:
        while True:
            text = recognize_speech()
            if text:
                if detect_trigger_words(text):
                    print("Trigger word detected!")
                    # Check the latest stress prediction
                    stress_level = check_stress()
                    if stress_level is not None:
                        if stress_level == 1:  # Assuming 1 indicates stress
                            print("Alert: High stress detected based on model prediction and trigger word!")
                        else:
                            print("Alert: Trigger word detected but no high stress predicted.")
            else:
                # Optionally, you can still check stress periodically if no speech is detected
                stress_level = check_stress()
                if stress_level == 1:
                    print("High stress detected based on model prediction.")
            sleep(10)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Alert system stopped by user.")
    finally:
        print("Exiting the alert system script.")

if __name__ == "__main__":
    main()
