school = {
    'teaching': [
        {'Name' : 'mohan', 'email' : 'mohan@gmail.com', 'subject': 'maths', 'phone': '54694569'},
        {'Name' : 'Rahul', 'email' : 'rahul@gmail.com', 'subject': 'physics', 'phone': '999999'}
    ],
    'admin' : [
        {'Name': 'Mohit', 'email' : 'MOhit@gmail.com', 'subject': 'Account', 'phone': '548954389'}
    ],
    'student' : {
        '9th' : [
            {'Name' : 'raju', 'email' : 'raju@gmail.com', 'phone': '535345345'}
        ],
        '10th' : [
            {'Name' : 'raghav', 'email' : 'raghav@gmail.com', 'phone': '554453453'},
            {'Name' : 'pavan', 'email' : 'pavan@gmail.com', 'phone': '4455455455'}
        ],
        '11th' : [
            {'Name' : 'sanu', 'email' : 'sanu@gmail.com', 'phone': '6565767'}
        ],
        '12th' : [
            {'Name' : 'shreshth', 'email' : 'shreshth@gmail.com', 'phone': '8778677877'}
        ]

    }

}

print(school['student']['10th'][1]['phone']) # 4455455455
print(school['student']['12th'][0]['Name'])
print(school['student']['10th'][1])
print("#"*50)
for key, value in school.items():
    print(key,":",value)
    if isinstance(value, dict):
        for k1,v1 in value.items():
            for data in v1:
                print(data['Name'])
    elif isinstance(value,list):
        for data in value:
            print(data['Name'])

print("$"*50)
# Get student details with his name
st_name= "raju"

for key, value in school.items():
    if isinstance(value,dict):
        for k1,v1 in value.items():
            for data in v1:
                if data['Name'] == st_name:
                    print(data)

print("#"*50)
# Home work.
# write a python code to get any personal email id on the basis of phone number.
ph_no = '548954389'
for key, value in school.items():
    if isinstance(value, dict):
         for k, v in value.items():
             for data in v:
                 if data['phone'] == ph_no:
                     print(data)
    elif isinstance(value, list):
        for data in value:
            if data['phone'] == ph_no:
                print(data)


# {'Name': 'Mohit', 'email': 'MOhit@gmail.com', 'subject': 'Account', 'phone': '548954389'}

