school = {
    'teaching': [
        {'Name': 'mohan', 'email': 'mohan@gmail.com', 'subject': 'maths', 'phone': '54694569'},
        {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'subject': 'physics', 'phone': '999999'}
    ],
    'admin': [
        {'Name': 'Mohit', 'email': 'MOhit@gmail.com', 'subject': 'Account', 'phone': '548954389'}
    ],
    'student': {
        '9th': [
            {'Name': 'raju', 'email': 'raju@gmail.com', 'phone': '535345345'}
        ],
        '10th': [
            {'Name': 'raghav', 'email': 'raghav@gmail.com', 'phone': '554453453'},
            {'Name': 'pavan', 'email': 'pavan@gmail.com', 'phone': '4455455455'}
        ],
        '11th': [
            {'Name': 'sanu', 'email': 'sanu@gmail.com', 'phone': '6565767'}
        ],
        '12th': [
            {'Name': 'shreshth', 'email': 'shreshth@gmail.com', 'phone': '8778677877'}
        ]

    }
}

# print(school['teaching'])
# print(school['teaching'][0])
# print(school['teaching'][0]['Name'])
# print(school['teaching'][0]['email'])
# print(school['teaching'][1])
# print(school['teaching'][1]['Name'])
# print(school['teaching'][1]['email'])
# print(school['admin'])
# print(school['student']['9th'])
# print(school['student']['10th'])
# print(school['student']['10th'][1]['phone'])     # 4455455455

# Print the name of all the persons associated with school

# get school key and value
for key, value in school.items():
    print(key, ":", value)
    if isinstance(value, dict):
        # get student keys and values
        for k1, v1 in value.items():
            # iterate over students details
            for data in v1:
                # print student name
                print(data['Name'])

    # Checking the new values received is list or not
    elif isinstance(value, list):
        # iterate over teachers and admin details
        for data in value:
            # print teacher and admin name
            print(data['Name'])
# Get student details with his name
st_name = "raju"

# iterate over schools keys and values
for key, value in school.items():
    # checking the student value in dict form
    # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
    if isinstance(value, dict):
        # iterate over student values
        for k1, v1 in value.items():
            # iterate over student details
            for data in v1:
                # get specific information as per the keys provided.
                if data['Name'] == st_name:
                    print(data)

# Homework #
# write a python code to get any personal email id on the basis of phone number.
