import pandas as pd
from os import walk

folder = "C:/Users/BADRINAR/Google Drive/Misc"
data_dict = {'Datetime': ['2017-10-10 22:27:00'], 'Status': ['Discharging'], 'Health': ['Good'], 'Level': [87], 'Scale': [100], 'Plugged': ['None'], 'Voltage': [4183], 'Temperature': [34.1]}
data = pd.DataFrame(data_dict, index=data_dict['Datetime'])
# data.set_index(pd.to_datetime(data['Datetime']), inplace=True)
for dirpath, dirname, filenames in walk(folder):
    for filename in filenames:
        print(dirpath, filename)
        df = pd.read_csv(dirpath + '/' + filename)
        df.set_index(pd.to_datetime(df['Datetime']), inplace=True)
        df = df.iloc[::-1]
        data = data.append(df)
        print(str(filename))
print(data)