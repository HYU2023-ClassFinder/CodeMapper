import sqlite3
conn = sqlite3.connect("CScourseDB.db", isolation_level=None)
c = conn.cursor()

# filename = 'nonCS.txt'
# f = open(filename, 'r')
# lines = f.readlines()

# for line in lines:
#     print(int(line))

#     nonCSID = int(line)
#     c.execute("delete from cur where lectureId = " + line)
#     c.execute("delete from review where lectureId = " + line)
#     c.execute("delete from tag where lectureId = " + line)
#     c.execute("delete from course where id = " + line)
#     conn.commit()
#-----------------------------------------------------------------
# c.execute('select * from tag')
# rawData = c.fetchall()

# # file = open("nonEngTag.txt", "w", encoding="UTF-8")
# koreanTag = ["코딩 테스트", "한컴오피스", "정보처리기사", "넥사크로", "전자정부프레임워크", 
#              "컴퓨터활용능력", "정보처리산업기사", "네이버 키워드 검색", "PC정비사", "빅데이터분석기사" ,"전산세무회계", "스마트스토어", "망고보드"]
# idkTag = ["업무 생산성", "협업 툴", "대인관계", "블록코딩", "콘텐츠 제작", "콘텐츠 기획", "시빅해킹"]
# nonEngTag = []

# koreanTagCount = 0
# idkTagCount = 0
# nonEngTagCount = 0

# # for _ in rawData:
# #     if(_[2].replace(' ', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('+', '').replace('-', '').replace('#', '').replace('/', '').replace('*', '').replace('&', '').encode().isalnum() == False
# #        and _[2] not in koreanTag
# #        and _[2] not in idkTag
# #        and _[0] < 5008):
# #         print(_[0], _[1], _[2])
# #         file.write(str(_[0]) + ' ' + str(_[1]) + ' ' + str(_[2]) + '\n')
# #         nonEngTag.append(_[2])
# # print(len(nonEngTag))
# # print(len(list(set(nonEngTag))))

# for _ in rawData:
#     if(_[2] in koreanTag):
#         koreanTagCount = koreanTagCount+1
#     if(_[2] in idkTag):
#         idkTagCount = idkTagCount+1
#     if(_[0] >= 5008 and _[2].replace(' ', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('+', '').replace('-', '').replace('#', '').replace('/', '').replace('*', '').replace('&', '').encode().isalnum() == False):
#         nonEngTagCount = nonEngTagCount+1

# print("koreanTagCount", koreanTagCount)
# print("idkTagCount", idkTagCount)
# print("nonEngTagCount", nonEngTagCount)

# # file.close()
#-----------------------------------------------------------------
# c.execute('select * from tag')
# rawData = c.fetchall()

# import collections

# tag = []

# for _ in rawData:
#     tag.append(_[2])
# tagCounter = collections.Counter(tag)
# # print(tagCounter)
# tagCount = [(key, value) for key,value in tagCounter.items()]
# tagCount.sort(key=lambda x : -x[1])
# tagCount = dict(tagCount)
# with open('tagCount.json', 'w') as f:
#     json.dump(tagCount, f, indent=4)
#-----------------------------------------------------------------
# import requests
# import pprint
# import json
 
# def fetch_wikidata(params):
#     url = 'https://www.wikidata.org/w/api.php'
#     try:
#         return requests.get(url, params=params)
#     except:
#         return 'There was and error'

# query = 'computer programming'
 
# # Which parameters to use
# params = {
#         'action': 'wbsearchentities',
#         'format': 'json',
#         'search': query,
#         'language': 'en'
#     }
 
# # Fetch API
# data = fetch_wikidata(params)

# #show response as JSON
# data = data.json()

# # with open('json_java.json', 'w') as f:
# #     json.dump(data, f, indent=4)
# possibleTag = []
# for i in range(len(data["search"])):
#     possibleTag.append(data["search"][i]["display"]["label"]["value"])
# if(possibleTag.count(query) == 1):
#     print("OK")
# print(possibleTag)
# # print(json.dumps(data, indent=4))
#------------------------------------------------------------------------------
import json
import requests
import pprint
import json
 
def fetch_wikidata(params):
    url = 'https://www.wikidata.org/w/api.php'
    try:
        return requests.get(url, params=params)
    except:
        return 'There was and error'

with open('tagCount.json', 'r', encoding="UTF-8") as f:
    tagCount = json.load(f)

conceptListCS = ["computer", "programming", "python", "learning", "data", "web", "linux", "operating system", "algorithm", "microsoft"]
tagMapping = []
for tag in tagCount:
    query = tag.split(":")[0]
 
    # Which parameters to use
    params = {
            'action': 'wbsearchentities',
            'format': 'json',
            'search': query,
            'language': 'en'
        }
    try:
    # Fetch API
        data = fetch_wikidata(params)
    except:
        code = "No_wikidata_tag"

    #show response as JSON
    data = data.json()
    code = ""
    
    
    possibleTag = []
    for i in range(len(data["search"])):
        for concept in conceptListCS:
            # print(data["search"][i])
            if("description" in data["search"][i] and "label" in data["search"][i] and concept in data["search"][i]["description"] and query == data["search"][i]["label"]):
                possibleTag.append(i)
                break
    if(len(possibleTag) == 1):
        code = data["search"][possibleTag[0]]["id"]
    elif(len(possibleTag) > 1):
        code = data["search"][possibleTag[0]]["id"]
    else:
        code = str(possibleTag.count(query)) + "_" + query.replace(' ', '_') + '_tags_in_wikidata'
    
    tagMapping.append((query, code))
    print((query, code))

tagMapping = dict(tagMapping)
with open('tagMapping.json', 'w') as f:
    json.dump(tagMapping, f, indent=4)
# conn.close()