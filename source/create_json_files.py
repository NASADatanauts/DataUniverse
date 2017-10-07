import nltk
import string
import numpy
from nltk.corpus import stopwords
from os import SEEK_END

from collections import Counter


my_data = numpy.recfromcsv('data.csv', delimiter='\r')
all_tags = []
unique_tags = []

# put tags of each line as nodes into the json file
for x in range(0, my_data.size):
    string = (my_data[(x)][0]).decode('utf8')
    newstr = string.strip()
    all_tags.append(newstr.split(','))

json_file = open("nodes.json", "w")
json_file.write("[")

# Remove whitespaces, remove "", add unique entries to connections
for tags in all_tags:
    for single_tag in tags:
        tagtoadd = single_tag.strip()
        tagtoadd = tagtoadd.replace('"', '')
        if not tagtoadd.isdigit():
            if tagtoadd not in unique_tags:
                unique_tags.append(tagtoadd)
                json_file.write("{")
                json_file.write("\"name\": \"" + tagtoadd + "\"")
                json_file.write("},")

# Remove last ,
json_file.seek(-1, SEEK_END)
json_file.truncate()

# Close JSON
json_file.write("]")
json_file.close

connected_tags = [[]] * len(unique_tags)


# create links between related tags and write to json file
json_links_file = open("links.json", "w")

json_links_file.write("[")

for lines in all_tags:
    for single_tag in lines:
        if single_tag in unique_tags:
            # print single_tag # tag gefunden
            for tagtoadd in lines:
                if not tagtoadd.strip().isdigit():
                    # in unique_tags:
                    if unique_tags.index(tagtoadd.strip()) != unique_tags.index(single_tag):
                        # print str(unique_tags.index(single_tag))+" "+str(unique_tags.index(tagtoadd.strip()))
                        json_links_file.write(
                            "{ \"source\": \"" + single_tag + "\",")
                        connected_tags[unique_tags.index(
                            single_tag)].append(tagtoadd)
                        json_links_file.write(
                            "\"target\": \"" + tagtoadd.strip() + "\"},")
            break

# Remove last ,
json_links_file.seek(-1, SEEK_END)
json_links_file.truncate()

json_links_file.write("]")
json_links_file.close
