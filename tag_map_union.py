input_udemy = open("tagmapping_temp.csv", "r")
input_wikibooks = open("wikibooks_tagmapping.csv", "r")
input_ucd = open("ucd_course_mapping.csv", "r")
output_file = open("tagmapping_union.csv", "w")

map = {}

for line in input_udemy.readlines():
    words = line.replace('"', '').split(",")
    map[words[1].replace('\n','')] = words[0].replace(" ", "_")
for line in input_wikibooks.readlines():
    words = line.replace('"', '').split(",")
    map[words[1].replace('\n','')] = words[0].replace(" ", "_")
for line in input_ucd.readlines():
    words = line.replace('"', '').split(",")
    map[words[1].replace('\n','')] = words[0].replace(" ", "_")

for key in map.keys():
    output_file.write('"' + map[key] + '","' + key + '"\n')