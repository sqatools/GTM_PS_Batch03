import requests
import json
"""
pip install requests
"""
def get_method_operation():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)
    for data in response.json():
        print(data)

#get_method_operation()

def post_method_operation():
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "3 TB"
            }
        })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("response code :", response.status_code)
    print(response.text)
    data = response.json()
    print(data)
    assert data['name'] == "Apple MacBook Pro 21" "name is not matching"


#post_method_operation()


def put_method_operation(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "3 TB"
            }
        })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print("response code :", response.status_code)
    print(response.text)
    data = response.json()
    print(data)
    assert data['name'] == "Apple MacBook Pro 20"



#put_method_operation("ff8081818fb998eb018fdc425632327d")


def patch_method_operation(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 100",
        })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    print("response code :", response.status_code)
    print(response.text)
    data = response.json()
    print(data)
    assert data['name'] == "Apple MacBook Pro 100"

patch_method_operation("ff8081818fb998eb018fdc425632327d")

def delete_method_operation(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    print("response code :", response.status_code)
    print(response.text)

#delete_method_operation("ff8081818fb998eb018fdc425632327d")
