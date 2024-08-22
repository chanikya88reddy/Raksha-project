import pandas as pd
import numpy as np
def simulate_data(n):
    heart_rate = np.random.normal(75, 10, n)
    hrv = np.array([np.std(np.diff(heart_rate)) for _ in range(n)])
    pvr = np.array([np.mean(heart_rate) * 0.1 for _ in range(n)])
    stress = np.random.choice([0, 1], size=n, p=[0.7, 0.3])  # 30% stressed
    data = pd.DataFrame({'heart_rate': heart_rate, 'hrv': hrv, 'pvr': pvr, 'stress': stress})
    return data
