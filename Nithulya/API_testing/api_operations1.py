
################### API Testing ######################################################################

#1).
# import requests
# import json
# def get_method_operation():
#     url = "https://api.restful-api.dev/objects"
#     payload = {}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)   #(OR)
#     #response = requests.get( url, headers=headers, data=payload)
#     print('Status code : ',response.status_code)
#     print(response.text)
#
#     for data in response.json():
#         print(data)
# get_method_operation()

#2).
# import requests
# import json
# def post_method_operation():
#     import requests
#     import json
#     url = "https://reqres.in/api/users"
#     payload = json.dumps({
#         "name": "Nivya",
#         "job": "Tester"
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     print('Status code : ',response.status_code)
#     print(response.text)
#     data = response.json()
#     assert data['name'] == 'Nivya'
#
# post_method_operation()

#3)
import requests
import json
def put_method_operation():

    url = "https://reqres.in/api/users/2"
    payload = json.dumps({
        "name": "Nivya",
        "job": "Teacher",
        "id": "714",
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)


put_method_operation()






