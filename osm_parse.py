#Run the following commands on your terminal before executing the code :


#sudo apt-get install osmctools
#sudo apt-get update


import numpy as np
import pandas as pd 


#osmconvert map.osm --all-to-nodes --csv="@id @lon @lat amenity shop name" --csv-headline -o=amenity.csv
#This command return a tab seperated values file which can be converted to csv as follows.

tsv_file='amenity.csv'
csv_table=pd.read_csv('amenity.csv',sep='\t')
csv_table.to_csv('amenity1.csv',index=False)


df = pandas.read_csv('amenity1.csv')
a = df['name'].notnull()
df1 =df[a]
#print (df1[['name','amenity','shop']])          #Prints shops in the area
shops = df1['shop'].notnull()
print(df1[shops])

print('\n')

amenities = df['amenity'].notnull()
amen = df[amenities]
print ("Hospitals in the area are :")
print (df[df.amenity.str.contains("hospital", na=False)])    #Prints amenities in the area


countx = df.amenity.str.contains("hospital", na=False)
print('\n')
print("No of hospitals in the area are :\n")
trues = np.count_nonzero(countx)
print (trues)



#osmconvert shops.osm --all-to-nodes --csv="@id @lon @lat building name" --csv-headline -o = buildings.csv
print('\n')
tsv_file='buildings.csv'
csv_table=pd.read_csv('buildings.csv',sep='\t')
csv_table.to_csv('buildings1.csv',index=False)

dfb = pandas.read_csv('buildings1.csv')
b = dfb['building'].notnull()                         #Prints buildings in the area
print(dfb[b])

#osmconvert map.osm --all-to-nodes --csv="@id @lon @lat power name voltage" --csv-headline -o=power.csv
print('\n')
tsv_file='buildings.csv'
csv_table=pd.read_csv('power.csv',sep='\t')
csv_table.to_csv('power1.csv',index=False)

dfp = pandas.read_csv('power1.csv')                     #Prints power lines in the area
p = dfp['power'].notnull()
print(dfp[p])




tsv_file='landcover.csv'
csv_table=pd.read_csv('landcover.csv',sep='\t')
csv_table.to_csv('landcover1.csv',index=False)

lc = pandas.read_csv('landcover1.csv')
l = lc['landuse'].notnull()
lu = lc[l]
print(lu[['@id','@lat','@lon','landuse']])                        #Prints land use in the area

print('\n')
 

natural = lc['natural'].notnull()
nat = lc[natural]
print(nat[['@id','@lat','@lon','natural']])

#print(df)















