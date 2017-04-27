# DataUniverse

Visual NASA Data Universe

Problem to be solved

The huge amounts of awesome open NASA data currently is not easily discoverable in a visual way in one place.
As a user, I need to know pretty clearly what I am looking for, when browsing e.g. data.nasa.gov.
The categories on the page are limited (Aerospace, Applied Science, Earth Science, Management/Operations, Space Science)

The data on data.nasa.gov is not complete.
The current way of finding data is either by using text search or by asking people directly.

Objectives:
*	Create a(n impressive ;)) visual representation of the data which can easily be explored via a website
*	Structure the data by topics (e.g. Earth, orbit, solar system, deep space, missions, general)
*	Be able to access each piece of API/data in 3 clicks max (3 levels)
*	Possibly use machine learning/crowdsourcing to classify data sources into topics
*	Enable datanauts to easily add newly found APIs and data sources

Use case:
I want to play with ISS data:
I can select „Orbit“ and find the „ISS“ there.
When selecting the ISS, I am seeing different kinds of data I can use:
A 3D model of the ISS, experiments that have been performed there, 360 VR videos, the location API.

I have found another interesting link to all missions that have been run so far, which I can add to the data (by drag&drop).


Implementation:
This is a first pass at a visual exploration for the 31k NASA APIs.

What it does:
1) getdata.py gets tags of API data from socrata and saves to data.csv (you can limit the number of APIs that are being requested) //TODO: later on, this should also save the description and URLs so that Datanauts can get to the API of interest fast
//TODO: the same info can basically be retrieved from the data.json file, so need to rewrite code to parse it

2) create_json_files.py creates the nodes and links json files which can be viewed in the data_universe.html //TODO: I wasn't able to delete the last comma in the json files yet, you need to do this manually ;)

Check out the example:
200 data points pulled and written to two json files (nodes and links)
