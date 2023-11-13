f = open("tagclaims_filtered_entities.txt", 'r')
csEntities = []
while True:
    line = f.readline()
    if not line: break
    csEntities.append(line)

tagClaims = []
f2 = open("tagClaims_v2_2.txt", 'r')
while True:
    line = f2.readline()
    if not line: break
    tagClaims.append(line)

f3 = open("tagClaims_v2_3.txt", 'r')
while True:
    line = f3.readline()
    if not line: break
    tagClaims.append(line)

import csv

f4 = open('tagmapping_union.csv','r', encoding='UTF8')
rdr = csv.reader(f4)
labelList = []
for line in rdr:
    labelList.append(line[1])
    print(line[1])

csTagClaims = []
for tagClaim in tagClaims:
    # if(tagClaim.split(" ")[0].replace("\n", "") in labelList):
    #     if(tagClaim.split(" ")[2].replace("\n", "") in labelList):
    #         print("good")
        
    if(tagClaim.split(" ")[0].replace("\n", "") in labelList and tagClaim.split(" ")[2].replace("\n", "") in labelList):
        csTagClaims.append(tagClaim)

f5 = open("csTagClaims_v4.txt", 'w')
for claim in csTagClaims:
    f5.write(claim)

