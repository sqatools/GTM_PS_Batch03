#1.
# import json
# def readJsonData(filename):
#     with open(filename,'r') as file:
#         data=file.read()
#         jsonData=json.loads(data)
#         return jsonData
# result=readJsonData("New Text Document.json")
# print(result)
# print("Name: ",result["Name"])
# print("Email: ",result["Email"])


#2.
import json
def write_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        jsonData=json.loads(data)
        jsonData['IP'] = '10.22.33.44'
        print(jsonData)
        updated_data = json.dumps(jsonData)
    with open(filename, "w") as file:
        file.write(updated_data)

write_json_data(r'C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\ExcelFileHandling\\New Text Document.json')

