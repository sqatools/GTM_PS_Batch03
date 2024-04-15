# 1). Python function program to add two numbers.
def add():
    num1 = 34
    num2 = 56
    print(f"Sum of {num1} and {num2}:", num1 + num2)


add()

def addition():
    num1 = 3
    num2 = 4
    return (num1 + num2)
s = addition()
print("Sum :",s)
print(addition())

def add1(num1, num2):
    total = num1+num2
    print(f"Sum of {num1} and {num2} is ", total)

add1(34,12)
# 2). Python function program to print the input string 10 times.

def strings():
    st1 = " Hello"
    return (st1*10)



print (strings() )

# 3). Python function program to print a table of a given number.


def table(num):
    for i in range (13):
        print(num, "*",i,"=", num*i)


table(3)



#4). Python function program to find the maximum of three numbers.

def min_max():
    lst = [34, -78, 56]
    mx = max(lst)
    mn  = min(lst)
    print("Min:", mn, "Max:",mx)

min_max()
print()
def largest(a, b, c):
    if a>b :
        if a>c:
            print("Max value :", a)
    elif b>a:
        if b>c:
            print("Max value :", b)
    else:
        print("Max value :", c)

num1 = 34
num2 = -67
num3 = 10

largest(num1, num2, num3)

def min(a, b , c):
    if a<b and a<c:
        print("Min value :", a)
    elif b<a and b<c:
        print("Min value :", b)
    else:
        print("Min value :", c)
min(-732, -45, 10)

# 5). Python function program to find the sum of all the numbers in a list.


def total(list1):
    total = 0
    for i in range(len(list1)):
        total =total +list1[i]
    print("The sum of elements of the given list :", total)

ls1 = [45, 67, 89,34]
total(ls1)

# 6). Python function program to multiply all the numbers in a list.

def pdt(list1):
    p =1
    for i in range(len(list1)):
        p = p* list1[i]
    print(f" The product of the values in the given list is {p}")


list2 = [12,34,1000,56]
pdt(list2)

# 7). Python function program to reverse a string.


def rev(string1):
    print(string1[::-1])

rev('String123')



# 8). Python function program to check whether a number is in a given range.

def in_range(num):
    if num in range(2,20):
        print(True)
    else:
        print(False)
a = int(input("Entr a number :"))
in_range(a)


# 9). Python function program that takes a list and returns a new list with unique elements of the first list.

def uni_list(list1):
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    return(list2)

l = [1,1,1,2,2,3,3,4,4,4,5]
l1 =uni_list(l)
print(l1)


# using set()
def unique(list1):
    print(list(set(list1)))

l = [1,1,1,2,2,3,3,4,4,4,5]
unique(l)


# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.

def prime(num):
    temp = 0
    for i in range(2,num):
        if num%i == 0:
            temp+=1

    if temp>0 :
        print(f"The number {num} is not prime")
    else:
        print(f"The number {num} is prime")


prime(11)
prime(12)





