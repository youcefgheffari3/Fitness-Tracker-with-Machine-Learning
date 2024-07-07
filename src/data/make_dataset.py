import pandas as pd
from glob import glob

data_path = '../../data/raw/MetaMotion/'
# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------
files = glob('../../data/raw/MetaMotion/*.csv')

def read_data_from_files(files) :
    acc_df = pd.DataFrame()
    gyr_df = pd.DataFrame()

    acc_set = 1
    gyr_set = 1

    for f in files :
        participant = f.split('-')[0].replace(data_path, '')
        label = f.split('-')[1]
        category = f.split('-')[2].rstrip('_MetaWear_2019').rstrip('123')

        df = pd.read_csv(f)
        df['participant'] = participant
        df['label'] = label
        df['category'] = category

        if 'Gyroscope' in f :
            df['set'] = gyr_set
            gyr_set += 1
            gyr_df = pd.concat([gyr_df, df])
        
        if 'Accelerometer' in f :
            df['set'] = acc_set
            acc_set += 1
            acc_df = pd.concat([acc_df, df])
    acc_df.index = pd.to_datetime(acc_df['epoch (ms)'], unit='ms')
    gyr_df.index = pd.to_datetime(gyr_df['epoch (ms)'], unit='ms')

    del acc_df['epoch (ms)']
    del acc_df['time (01:00)']
    del acc_df['elapsed (s)']

    del gyr_df['epoch (ms)']
    del gyr_df['time (01:00)']
    del gyr_df['elapsed (s)']
    
    return acc_df, gyr_df
    
acc_df, gyr_df = read_data_from_files(files)   
    

# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------