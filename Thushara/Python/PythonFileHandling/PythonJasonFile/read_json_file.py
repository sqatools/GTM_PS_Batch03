import json
def read_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data


result = read_json_data("test_json_content.json")
print(result)
print("Name :", result["Name"])
print("Name :", result["Email"])



