# import requests
# from bs4 import BeautifulSoup
# from html_table_parser import parser_functions
# import pandas as pd

# url = 'https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all'

# # response = requests.get(url)

# # if response.status_code == 200:
# #     html = response.text
# #     soup = BeautifulSoup(html, 'html.parser')
# #     # id = soup.select_one('#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(1) > td:nth-child(1)')
# #     # print(id)
# #     # label = soup.select_one('#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(1) > td:nth-child(2)')
# #     # print(label)
# #     tag = soup.select_one('#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(1)')
# #     print(tag)
# # else : 
# #     print(response.status_code)

# requests = requests.get(url)
# html = requests.text
# soup = BeautifulSoup(html, 'html.parser')

# data = soup.find("table", {"class":"wikitable"})
# table = parser_functions.make2d(data)

# df = pd.DataFrame(data=table[1:], columns=table[0])
# print(df)
# print(df.iloc[:, 0:2])

# df.to_csv('wikidataRelationCode.csv')

import csv
 
f = open('wikidataRelationCode.csv','r', encoding='UTF8')
rdr = csv.reader(f)
idList = []
labelList = []
for line in rdr:
    idList.append(line[1])
    labelList.append(line[2].replace(' ', '_'))

f2 = open("tagClaims.txt", 'r')
tagClaims = []
while True:
    line = f2.readline()
    if not line: break
    tagClaims.append(line)

f3 = open("tagClaims_v2.txt", 'w')
tagClaims_v2 = []
for tagClaim in tagClaims:
    splittedTagClaim = tagClaim.split()
    
    idx = idList.index(splittedTagClaim[1])
    splittedTagClaim[1] = splittedTagClaim[1] + '_' + labelList[idx]

    tagClaims_v2.append(splittedTagClaim[0] + ' ' + splittedTagClaim[1] + ' ' + splittedTagClaim[2])

for claim in tagClaims_v2:
    f3.write(claim)
    f3.write("\n")

f.close()
f2.close()
f3.close()