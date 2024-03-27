# question1
s1 = "IPL2024 CRICKET TROPHY"
first_char =s1[0]
last_char = s1[-1]
remaining_part = s1[1 : -1]
result = f"{last_char}{remaining_part}{first_char}"
print("result : ", result)

# question2
i = input("Enter sentence : ")
j = " "
k = 1
for k in range(len(i)):
    if k%2:
        j+=i[k]*2
    else:
        j+=i[k]
print(j)

# question 3
s2 = "GOOD MORNING"
first_char =s2[0]
last_char = s2[-1]
remaining_part = s2[-2: 0 : -1]
result = f"{last_char*2}{remaining_part}{first_char*2}"
print("result : ", result)