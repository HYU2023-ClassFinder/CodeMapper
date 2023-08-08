udemy = open("tagclaims_v2.csv", "r")
ucd = open("ucd_course_precedence.csv", "r")
udemy_filtered = open("tagclaims_filtered_relations.txt", "r")
wikibooks = open("wikibooks_prereq.csv", "r")

udemy_entities = set()
ucd_entities = set()
udemy_filtered_entities = set()
wikibooks_entities = set()

for line in udemy.readlines():
    words = line.split(",")
    udemy_entities.add(words[0])

for line in ucd.readlines():
    words = line.split(",")
    ucd_entities.add(words[0])

for line in udemy_filtered.readlines():
    words = line.split()
    udemy_filtered_entities.add(words[0])

for line in wikibooks.readlines():
    words = line.split(",")
    wikibooks_entities.add(words[0])

udemy_ucd_entities = udemy_entities.intersection(ucd_entities)
filtered_ucd_entities = udemy_filtered_entities.intersection(ucd_entities)
wikibooks_ucd_entities = wikibooks_entities.intersection(ucd_entities)
udemy_wikibooks_entities = udemy_entities.intersection(wikibooks_entities)
filtered_wikibooks_entities = udemy_filtered_entities.intersection(wikibooks_entities)

print("Number of Udemy entities: " + str(len(udemy_entities)))
print("Number of UCD entities: " + str(len(ucd_entities)))
print("Number of Udemy Filtered entities: " + str(len(udemy_filtered_entities)))
print("Number of Wikibooks entities: " + str(len(wikibooks_entities)))
print("Number of Udemy X UCD entities: " + str(len(udemy_ucd_entities)))
print("Number of Udemy Filtered X UCD entities: " + str(len(filtered_ucd_entities)))
print("Number of Wikibooks X UCD entities: " + str(len(wikibooks_ucd_entities)))
print("Number of Udemy X Wikibooks entities: " + str(len(udemy_wikibooks_entities)))
print("Number of Udemy Filtered X Wikibooks entities: " + str(len(filtered_wikibooks_entities)))
