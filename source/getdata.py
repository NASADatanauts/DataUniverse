#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import urllib2


limit = 100 #there are around 31k NASA data sets, this pulls [limit] number of data sets
json_file='http://api.us.socrata.com/api/catalog/v1?q=nasa&domains=data.nasa.gov&offset=0&limit='+str(limit)

json_data=urllib2.urlopen(json_file)
data = json.load(json_data)
		
html_file = open('data.csv', "w")


#writing the domain_tags to the data.csv file (there are other fields, such as link, name of the data source etc, which are not currently used
for x in range(0, limit):
	tags = (', '.join(data['results'][x]['classification']['domain_tags']))#+';'+data['results'][x]['permalink']+ ';'+data['results'][x]['resource']['description']+ ';'+data['results'][x]['resource']['name']
	stringtowrite = tags+'\n'
	html_file.write(stringtowrite.encode('utf8'))
	
	#print what comes back from the api
	#print(data['results'][x]['resource']['name'])
	#print(data['results'][x]['resource']['description'])
	#print(data['results'][x]['permalink'])
	#print(data['results'][x]['classification']['domain_tags'])
json_data.close()
html_file.close 