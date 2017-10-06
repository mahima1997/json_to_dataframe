# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:31:22 2017

@author: mah
"""

#Conversion to dataframe

import pandas as pd
import json
from pandas.io.json import json_normalize

#reading json file
json_data=open('data.json').read()
data = json.loads(json_data)

#print(data['interventions'][0]['name'])
#print(data['interventions'][1])

#list of keys present on json
primary_keys=data.keys()        #primary_keys is a list
#print primary_keys[2]
for key in primary_keys:
    print(key)

for key, value in data.items():
    print(key, value)

#converting list of dictionaries into dataframe
normalized_json=json_normalize(data['outcomes'])
print(normalized_json)

print(type(data))   #dict
print(type(data['control']))    #NoneType
print(type(data['interventions']))  #list
print(type(primary_keys[0]))    #unicode
print(type(primary_keys[1]))    #unicode
print(type(data['phases']))     #list
print(type(data['phases'][0]))  #unicode

#extending the above to all the keys in file
for key in primary_keys:
    if(type(data[key])==type(data['interventions']) and type(data[key][0])==type(data)):
        normalized_json=json_normalize(data[key])
        print(key,'/',normalized_json)
    elif(type(data[key])==type(data['interventions']) and type(data[key][0])==type(data['phases'][0])):
        print(pd.DataFrame({key:data[key]}))        
        #print(pd.DataFrame.from_items(data[key]))  
    else:
        print(data[key])

#converting list of dictionaries to dictionary of lists
interventions={}
for d in data['interventions']:
     for k,v in d.items():
         try:
             interventions[k].append(v)
         except KeyError:
             interventions[k]=[v]
print (interventions)
