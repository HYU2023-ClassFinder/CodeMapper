input_file = open("tagClaims_v2.txt", "r")
output_entities = open("tagclaims_filtered_entities.txt", "w")
output_file = open("tagclaims_filtered_relations.txt", "w")

# Read the input file
lines = input_file.readlines()

list_entities_direct = []

relevant_relations = ["P361_part_of", "P279_subclass_of", "P2579_studied_by", "P366_has_use", "P2283_uses"]
core_entities = ["Q21198", "Q630608", "Q2374463", "Q190637"] # computer_science, software_development, data_science, web_design
# somehow web design is not part of software development but of design

for line in lines:
    # Split the line into words
    words = line.split()
    if words[1] in relevant_relations and words[2] in core_entities:
        list_entities_direct.append(words[0])

set_entities = set(list_entities_direct)
previous_size = -1
while len(set_entities) != previous_size:
    for line in lines:
        words = line.split()
        if words[1] in relevant_relations and words[2] in set_entities:
            set_entities.add(words[0])
    previous_size = len(set_entities)

for entity in set_entities:
    output_entities.write(entity + "\n")

for line in lines:
    words = line.split()
    if words[0] in set_entities:
        output_file.write(line)