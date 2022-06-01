#Initialize DataFrame
import pandas as pd
df=pd.DataFrame(columns=['location','lat','lon'])
df['location']=['ViC','ACT','NSW']
df['lat']=[31.45,99.99,89.00]
df['lon']=[-170.58,-90.00,-190.88]

#USer provided lat and lon   22.22,-222.22
newlat=22.22
newlon=-222.22

#Import trig stuff from math
from math import sin, cos, sqrt, atan2,radians

#Distance function between two lat/lon
def getDist(lat1,lon1,lat2,lon2):
  R = 637.0

  lat1 = radians(lat1)
  lon1 = radians(lon1)
  lat2 = radians(lat2)
  lon2 = radians(lon2)

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))
  return R * c

  #Apply distance function to dataframe
df['dist']=list(map(lambda k: getDist(df.loc[k]['lat'],df.loc[k]['lon'],newlat,newlon), df.index))

 #This will give all locations within radius of 60 km
df[df['dist']<60]
print(df)
