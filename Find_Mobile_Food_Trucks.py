#importing pandas
import pandas as pd
#Getting Latitude and Longitude as user input
lat=input('Enter Latitude:')
long=input('Enter Longitude:')
#app = input('Enter Applicant: ')
#locid = input('Enter location id: ')
df= pd.read_csv('Mobile_Food_facility_Permit.csv')
#df = df.loc[df.Latitude == lat]
#Below command works fine and returns rows matching the criteria
df1=df.loc[(df['Applicant'] == 'Cochinita') & (df['locationid'] == 1591822)]
#Below command gives an error as I still need to resolve data type issue, lat and lon is float64 which is causing a streing search on these instead of numeric value match
#df1=df.loc[(df['Applicant'] == app) & (df['locationid'] == locid)]
df1=df.loc[(df['Latitude'] == lat) & (df['Longitude'] == long)]
#print(df1)
