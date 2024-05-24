study_center = {
    'tutors':[
              {'Name': 'Rafeeq', 'email': 'rafeeq@gmail.com', 'phone': '678678', 'Subject': 'Maths'},
              {'Name': 'Biju', 'email': 'biju@gmail.com', 'phone': '345676', 'Subject': 'English'},
              {'Name': 'Ajith', 'email': 'ajith@gmail.com', 'phone': '897342', 'Subject': 'Malayalam'},
              {'Name': 'Nandan', 'email': 'nandan@gmail.com', 'phone': '678678', 'Subject': 'Physics'}
             ],
    'students': {
            '8th': [
                        {'Name': 'Reena', 'email': 'reena@gmail.com', 'phone': '0987656'},
                        {'Name': 'Ramya', 'email': 'ramya@gmail.com', 'phone': '678978'},
                        {'Name': 'Maya', 'email': 'maya@gmail.com', 'phone': '6891261'}
                    ],
            '9th':  [
                        {'Name': 'Shafi', 'email': 'shafi@gmail.com', 'phone': '9675756'},
                        {'Name': 'Nisha', 'email': 'nisha@gmail.com', 'phone': '678987'},
                        {'Name': 'Hari', 'email': 'hari@gmail.com', 'phone': '6564329'}
                    ],
            '10th': [
                        {'Name': 'Keerthi', 'email': 'keerthi@gmail.com', 'phone':'558678'},
                        {'Name': 'Ammu', 'email': 'ammu@gmail.com', 'phone': '7778678'},
                        {'Name': 'Veena', 'email': 'veena@gmail.com', 'phone': '338678'}
                    ]

}
}
for keys, values in study_center.items():
    print(keys, ":", values)
    if isinstance(values,dict):
        for key, val in values.items():
            for data in val:
                print(data['Name'])
    elif isinstance(values, list):
        for data in values:
            print(data['Name'])

print("#"*50)
for key, value in study_center.items():
    if isinstance(value, list):
        for data in value:
            print(data['Name'], ":",data['Subject'])

            if isinstance(value,dict):
                for k,v in value.items():
                    for data in v:
                        print(data['Name'])

print("#"*50)

for key , val in study_center.items():
    if isinstance(val, dict):
        for k,v in val.items():
            for data in v:
                print("Student", ":",data["Name"])

    if isinstance(val, list):
        for data in val:
            print("Tutor", ":", data["Name"])

print("$"*50)
print(study_center['students']['9th'][1])
print(study_center['tutors'][2].items()) # dict_items([('Name', 'Ajith'), ('email',
# 'ajith@gmail.com'), ('phone', '897342'), ('Subject', 'Malayalam')])


