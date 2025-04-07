import json
dict = [
    {
    "empID": "1",
    "empName": "Ashwin",
    "salary": "50000"
    },

    {
    "empID": "2",
    "empName": "Aravind",
    "salary": "50000"
    },

    {
    "empID": "3",
    "empName": "Akhilesh",
    "salary": "100000"
    }
]

#Apply Serialization - Converting py object to json object
json_obj = json.dumps(dict)

#Write
with open("Pratice/FileHandling/JSON_Handling/data.json", "w") as outFile:
    outFile.write(json_obj)

