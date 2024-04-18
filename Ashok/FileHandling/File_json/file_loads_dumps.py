"""
The json.loads() takes in a string and returns a python dictionary and the
json.dumps() takes in a Python dictionary and returns a JSON string.

"""
import json

json_string = '''
   {
    "students": [
    {
        "id": 2,
        "email": "janet2.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
        "id": 3,
        "email": "janet3.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
        "id": 4,
        "email": "janet4.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }
    ]
}
'''
# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
# It is used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.

data = json.loads(json_string)  # Converting the string to dictionary.
print(data)
print(data['students'])  # fetching the data from dictionary
print(data['students'][0])

# json.dumps() method can convert a Python object into a JSON string
data1 = json.dumps(data)   # Converting the dictionary to string.
print(data1)

# Converting the dictionary to string.
# indent will provide spaces for json format.
# sort_keys=True, this will sort the keys in json object.
data1 = json.dumps(data, indent=2, sort_keys=True)   # Converting the dictionary to string.
print(data1)


