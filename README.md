# DataUniverse

This is a first pass at a visual exploration for the 31k NASA APIs. 
The (python) code pulls data from socrata and creates a data.csv

What it does:
1) getdata.py gets tags of API data from socrata and saves to data.csv (you can limit the number of APIs that are being requested)
TODO: later on, this should also save the description and URLs so that Datanauts can get to the API of interest fast

2) create_json_files.py creates the nodes and links json files which can be viewed in the data_universe.html
TODO: I wasn't able to delete the last comma in the json files yet, you need to do this manually

Check out the example:
200 data points pulled and written to two json files (nodes and links)
