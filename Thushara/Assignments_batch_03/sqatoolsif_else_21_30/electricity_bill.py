"""
29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill

"""
units = 350
bill = float()
if units <= 50:
    print("Bill :", units*0.50)
elif units <= 100:
    print("Bill :", units * 0.75)
elif units <= 2.50:
    print("Bill :", units * 1.25)
else:

    bill = units*1.50
    sur = (bill*17)/100

    print("Bill :", bill+sur)