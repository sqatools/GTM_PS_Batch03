# 10). Python program to validate user_id in the list of user_ids.
user_id = [102, 106, 107, 109]

id1 = int(input("Enter user_id :"))
if id1 in user_id:
    print("Valid ID")
else:
    print("Invalid ID")