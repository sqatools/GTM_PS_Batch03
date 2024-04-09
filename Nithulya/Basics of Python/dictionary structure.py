# school = {
#     'teaching': [
#         {'Name' : 'Riya', 'email' : 'riya@gmail.com', 'subject': 'Science', 'phone': '5555555555'},
#         {'Name' : 'Rinku', 'email' : 'rinku@gmail.com', 'subject': 'Zoology', 'phone': '6666666666'}],
#     'admin' : [
#         {'Name': 'Anju', 'email' : 'anju@gmail.com', 'subject': 'MCOM', 'phone': '7777777777'}],
#     'student' : {
#         '9th' : [{'Name' : 'Rini', 'email' : 'rini@gmail.com', 'phone': '8888888888'}],
#         '10th' : [{'Name' : 'Shahana', 'email' : 'shahana@gmail.com', 'phone': '1010101010'},
#                   {'Name' : 'Dona', 'email' : 'dona@gmail.com', 'phone': '1021021021'}],
#         '11th' : [{'Name' : 'Aleena', 'email' : 'aleena@gmail.com', 'phone': '1111111111'}],
#         '12th' : [{'Name' : 'Teena', 'email' : 'teena@gmail.com', 'phone': '1212121212'}]
#                  }
#          }
# print(school)
#######################################################################################################
# print(school['teaching'][1]['Name'],':',school['teaching'][1]['subject'])               # Rinku : Zoology
# print(school['admin'][0]['Name'],':',school['admin'][0]['email'])                       # Anju : anju@gmail.com
# print(school['student']['10th'][1]['Name'],':',school['student']['10th'][1]['phone'])   # Dona : 1021021021
# print(school['student']['11th'][0]['Name'],':',school['student']['11th'][0]['email'])   # Aleena : aleena@gmail.com
# print(school['student']['12th'][0]['Name'],':',school['student']['12th'][0]['email'])   # Teena : teena@gmail.com


#1.
# for key, value in school.items():
#     if isinstance(value, dict):
#         for k1, v1 in value.items():
#             for v2 in v1:
#                 print(v2['email'])


#2.
# for key, value in school.items():
#     if isinstance(value, dict):
#         for k1, v1 in value.items():
#             for v2 in v1:
#                 print(v2['email'])
#     elif isinstance(value, list):
#         for v3 in value:
#             print(v3['subject'])

#3. Get student details with her name, studName='Dona'
# studName='Dona'
# for key,value in school.items():
#     if isinstance(value,dict):
#         for k1,v1 in value.items():
#             for value1 in v1:
#                 if value1['Name']==studName:
#                     print(value1)               # {'Name': 'Dona', 'email': 'dona@gmail.com', 'phone': '1021021021'}



#4. Write a python code to get any personal email id on the basis of phone number.
#1.
# studPhone='7777777777'
# for key,value in school.items():
#     if isinstance(value,list):
#         for v1 in value:
#             if v1['phone']==studPhone:
#                 print(v1['email'])           # anju@gmail.com


#2.
# studPhone='1111111111'
# for key,value in school.items():
#     if isinstance(value,dict):
#         for k1,v1 in value.items():
#             for v2 in v1:
#                 if v2['phone']==studPhone:
#                     print(v2['email'])


#2.
office={
'Administration':[{'Name' : 'Riya', 'email' : 'riya@gmail.com', 'phone': '5555555555'},
        {'Name' : 'Rinku', 'email' : 'rinku@gmail.com', 'phone': '6666666666'}],
'Financial':[{'Name': 'Aniya', 'email' : 'aniya@gmail.com','phone': '4444444444'},
          {'Name': 'Anju', 'email' : 'anju@gmail.com','phone': '7777777777'}],

'IT':   {
    'Developer':({'Name' : 'Sunil', 'email' : 'sunil@gmail.com', 'phone': '1010101020'},
                 {'Name' : 'Sumisha', 'email' : 'sumisha@gmail.com', 'phone': '1010101030'},
                 {'Name' : 'Sajira', 'email' : 'sajira@gmail.com', 'phone': '1010101040'},
                 {'Name' : 'Sreeshma', 'email' : 'sreeshma@gmail.com', 'phone': '1010101050'}),
      'Tester':({'Name' : 'Nithya', 'email' : 'nithya@gmail.com', 'phone': '9910101010'},
                {'Name' : 'Navami', 'email' : 'navami@gmail.com', 'phone': '9910101020'},
                {'Name' : 'Nihar', 'email' : 'nihar@gmail.com', 'phone': '9910101030'},
                {'Name' : 'Neethu', 'email' : 'neethu@gmail.com', 'phone': '9910101040'})
        },
'CustomerService':[{'Name' : 'Rini', 'email' : 'rini@gmail.com', 'phone': '8888888888'},
           {'Name' : 'Shahana', 'email' : 'shahana@gmail.com', 'phone': '1010101010'},
           {'Name' : 'Dona', 'email' : 'dona@gmail.com', 'phone': '1021021021'}],
    'HR':({'Name' : 'Hari', 'email' : 'hari@gmail.com', 'phone': '9988888888'},
          {'Name' : 'Hridhya', 'email' : 'hridhya@gmail.com', 'phone': '8888888888'})
     }

# print(office['IT']['Developer'][1]['Name'])
#1.
# name1='Navami'
# for key,value in office.items():
#     if isinstance(value,dict):
#         for k1,v1 in value.items():
#             for v2 in v1:
#                 if v2['Name']==name1:
#                     print(v2['email'])              # navami@gmail.com


#2.
name1='Navami'
for key,value in office.items():
    if isinstance(value,dict):
        for k1,v1 in value.items():
            for v2 in v1:
                if v2['Name']==name1:
                    print(v2['email'])          # navami@gmail.com
    elif isinstance(value,tuple):
        for v3 in value:
            if v3['Name']=='Hari':
                print(v3['email'])              # hari@gmail.com



