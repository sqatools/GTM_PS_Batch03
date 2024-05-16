'''
%j - Day of the year as a zero added decimal number.
%B - Full month name.
%A - Full weekday name.
%a - Abbreviated weekday name.
%S - Second as a zero added decimal number.
%Z - Time zone name.
'''

from datetime import datetime

print(datetime.now().date())    # 2024-05-15
print(datetime.now().day)       # 15
print(datetime.now().month)     # 5
print(datetime.now().year)      # 2024

var1 = datetime.now().strftime('%m/%d/%Y %H:%M:%S %A')
print(var1)                           # 05/15/2024 13:42:36 Wednesday

#2.
# from datetime import datetime
# s = datetime.now().strftime("%a-%m-%y")
# print('Result :', s)           # Result : Wed-05-24

#3.
# from datetime import datetime
# s = datetime.now().strftime("%A %m %Y")
# print('Result:', s)              # Result: Wednesday 05 2024

#4.
# from datetime import datetime
# s = datetime.now().strftime("%I %p %S")
# print('Result:', s)             # Result: 01 PM 26

#5.
# from datetime import datetime
# s = datetime.now().strftime("%j")
# print('Result:', s)                 # Result: 136