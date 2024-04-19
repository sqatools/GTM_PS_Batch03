import json
def readJsonData(filename):
    with open(filename,'r') as file:
        data=file.read()
        jsonData=json.loads(data)
        return jsonData
result=readJsonData("New Text Document.json")
print(result)
print("Name: ",result["Name"])
print("Email: ",result["Email"])

