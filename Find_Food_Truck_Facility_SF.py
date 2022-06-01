# Import math and numpy functions
import math
import numpy as np
#Import Pandas to create dataframe
import pandas as pd
#Initialise Pandas Dataframe using Mobile_Food_Facility_Permit.csv
# Read csv with dtype as str so that data type of latitude and longitude is not changed during dataframe creation
csv_seperator = ','
df = pd.read_csv('Mobile_Food_Facility_Permit.csv', dtype='str', sep=csv_seperator)
# Assign Latitude column to sort_lan - a new column in df with type conversion to float64 and assign latitude column to sort_lon a new column in df
df['sort_lat']=df['Latitude'].astype('float64')
df['sort_lon']=df['Longitude'].astype('float64')
print("Original csv and two more columns")
print(df)
# Create new csv with less columns for easy troubleshooting of code, rest of the columns will be included in df1 once program works without errors
df1=pd.DataFrame(columns=['locationid','lat','lon'])
print(df1) # it will be empty dataframe as of now
df1['locationid']=df['locationid']
df1['lat']=df['sort_lat']
df1.round(2)
print(df1['lat'])
df1['lon']=df['sort_lon']
print(df['sort_lon'])
print("Subset of csv with only few columns")
print(df1)
#User input for latitude and longitude
newlat=input("Enter value for Latitude: ")
newlon=input("Enter value for Longitude: ")
print(newlat)
print(newlon)
# Fixed values for lat and lon that were used to test program   39.54,-114.20
#newlat=39.54
#newlon=-114.20

#Import trig functions from math package
from math import sin, cos, sqrt, atan2,radians

#Calculate distance between user input latitude and longitude and latitude's, longitude's in the csv to display nearest Food Trucks based on user co-ordinates
def getDist(lat1,lon1,lat2,lon2):
  R = 6373.0

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
df1['dist']=list(map(lambda k: getDist(df1.loc[k]['lat'],df1.loc[k]['lon'],newlat,newlon), df1.index))

 #This will give all locations within radius of 60 km
df1[df1['dist']<60]
print(df1)
