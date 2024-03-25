# 12). Python program to describe the interview process.

round1 = input("Enter round 1 results :")
round2 = input("Enter round 2 results :")
if round1 == "passed":
    if round2 == "passed":
        print("Congrats you are placed!")
    else:
        print("You have not cleared 2nd round. Try again later.")
else:
    print("You have not cleared first round. Try again later.")