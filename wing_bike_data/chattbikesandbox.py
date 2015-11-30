import pandas as pd
import matplotlib as plt

b = pd.read_csv("../bike_data/bike_data.csv")

stations = b['StartStationName'].unique()
print(stations[:],sep="\n",file="stations.txt")
melt=pd.melt(b,id_vars='StartStationName')

bbystart = b.groupby('StartStationName')

print('end of program')