import pandas as pd
import datetime
import numpy as np
import matplotlib.pylab as plt


data = pd.read_json('hr_data.json')

pd.options.mode.chained_assignment = None

df = data


j = 0

for i in df.Time:
   df['Time'][j] = datetime.datetime.fromtimestamp(i / 1000).strftime('%Y-%m-%d %H:%M:%S')
   df['Time'][j] = datetime.datetime.strptime(str(df['Time'][j]), "%Y-%m-%d %H:%M:%S").time()
   j += 1


df_time_str =df['Time'].astype(str)

pd.to_datetime(df_time_str)

df_index = df.set_index('Time')

print(df_index.head())
plt.plot(df.Time, df.RRInterval)
plt.xlabel('Time Span ')
plt.ylabel('RRInterval')

plt.show()











