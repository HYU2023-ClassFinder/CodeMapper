import json
import requests
import pprint

with open("tagMapping.json", "r") as tagMapping:
    tagList = json.load(tagMapping)

tag = []
for key, value in tagList.items():
    tag.append(value)
tag = list(set(tag))
# print(tag)

def fetch_wikidata(params):
    url = 'https://www.wikidata.org/w/api.php'
    try:
        return requests.get(url, params=params)
    except:
        return 'There was and error'
    
claims = []
keyerror = open("keyerror.txt", "w")
for _tag in tag:
    # Which parameters to use
    params = {
            'action': 'wbgetentities',
            'ids': str(_tag),
            'format': 'json',
            'language': 'en'
        }
    try:
    # Fetch API
        data = fetch_wikidata(params)
    except:
        code = "No_wikidata_tag"

    data = data.json()
    # pprint.pprint(data["entities"][str(_tag)]["claims"])

    try:
        for key, value in data["entities"][str(_tag)]["claims"].items():
            for i in range(len(value)):
                # print(value[i]["mainsnak"]["property"])
                try:
                    # print(value[i]["mainsnak"]["datavalue"]["value"]["id"])
                    claims.append(str(_tag) + " " + value[i]["mainsnak"]["property"] + " " + value[i]["mainsnak"]["datavalue"]["value"]["id"])
                    print(str(_tag) + " " + value[i]["mainsnak"]["property"] + " " + value[i]["mainsnak"]["datavalue"]["value"]["id"])
                except:
                    pass
    except KeyError:
        keyerror.write(str(_tag) + " key error")
        keyerror.write("\n")
        print(str(_tag) + " key error")
        pass

tagClaims = open("tagClaims.txt", "w")
for claim in claims:
    tagClaims.write(claim)
    tagClaims.write("\n")
tagClaims.close()
keyerror.close()