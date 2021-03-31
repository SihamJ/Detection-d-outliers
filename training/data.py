import numpy as np
import pandas as pd

# define features and target values
data = {
    'wind_direction': ['N', 'S', 'E', 'W'],
    'tide': ['Low', 'High'],
    'swell_forecasting': ['small', 'medium', 'large'],
    'good_waves': ['Yes', 'No']
}

# create an empty dataframe
data_df = pd.DataFrame(columns=data.keys())

np.random.seed(42)
# randomnly create 1000 instances
for i in range(1000):
    data_df.loc[i, 'wind_direction'] = str(np.random.choice(data['wind_direction'], 1)[0])
    data_df.loc[i, 'tide'] = str(np.random.choice(data['tide'], 1)[0])
    data_df.loc[i, 'swell_forecasting'] = str(np.random.choice(data['swell_forecasting'], 1)[0])
    data_df.loc[i, 'good_waves'] = str(np.random.choice(data['good_waves'], 1)[0])

data_df.head()