import json


#Apply Deserialization --> Converting json obj to py obj
with open("Pratice/FileHandling/JSON_Handling/data.json", "r") as readFile:
    res = json.load(readFile)
    

for data in res:
    print(data)