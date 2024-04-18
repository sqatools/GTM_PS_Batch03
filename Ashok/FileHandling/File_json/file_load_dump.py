import json

# json.load() takes a file object and returns the json object. It is used to read JSON encoded data
# from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts a
# file object.

with open("json_data1.json", "r") as f:
    data = json.load(f)
    print(data)
    print(data['Name'])
    print(data['Email'])

# while the json. dump() function is used to serialize a Python object into a JSON formatted string
# and write it to a file-like object.

with open("json_data2.json", "w") as f1:
    json.dump(data, f1)

with open("json_data3.json", "w+") as f2:
    json.dump(data, f2)

with open("json_data4.json", "x") as f3:
    json.dump(data, f3)
