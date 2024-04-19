import json


def read_json_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        print(data)
        print(data["Name"])
        print(data["Email"])


read_json_data("json_data.json")


def read_json_data1(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data


result = read_json_data1("json_data.json")
print(result)
print("Name :", result["Name"])
