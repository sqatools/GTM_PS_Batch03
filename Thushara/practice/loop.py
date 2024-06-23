num = 1
for i in range(5):
    for j in range(i+1):
        print(num,end =" ")
        num+=1
    print()


for i in range(5):

    for j in range(i+1):
        num1 = 1
        print(num1, end=" ")
        num1 += 1
    print()
num1 =1
for k in range(5, 0, -1):
    for l in range(k-1):
        num1 -= 1
        print(num1, end=" ")
    print()


print("$"*50)
num2 =1
for i in range(5):
    for j in range(i+1):
        print(num2,end=" ")
        num2+=1
    print()
for k in range(5,0,-1):
    for l in range(k-1):
        print(num2,end =" " )
        num2 += 1
    print()



num = 65
for i in range (5):
    for j in range(i+1):
        print(chr(num),end=" ")
        num +=1
    print()
for k in range (5,0,-1):
    for l in range(k-1):
        print(chr(num),end=" ")
        num += 1
    print()




