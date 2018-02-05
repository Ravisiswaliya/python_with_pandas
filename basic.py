import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# creating data
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_Rate':[65,72,62,64,54,66]}

#reading data
df = pd.DataFrame(web_stats)

#print(df.head()) #reading first 5 dataframe
#print(df.tail()) #reading last 5 dataframe

df = df.set_index('Day') #day column as index
#print(df[['Visitors','Bounce_Rate']])      #accessiing selected column

#print(df.Visitors.tolist())  #convert column to list

print(np.array(df[['Visitors','Bounce_Rate']]).tolist())     #convert multiple column into list

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))
print(df2)


