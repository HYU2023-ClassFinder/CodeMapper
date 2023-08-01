from collections import Counter

f = open("tagClaims_v2.txt", 'r')
relation = []
while True:
    line = f.readline()
    if not line: break
    relation.append(line.split(" ")[1])

relation = Counter(relation)
for key, value in relation.items():
    print(key, value)
    
print(len(relation))

f.close()