# Python program to calculate simple interest.
# Formula: SI = p*r*t
p = int(input("Principle Amount :"))
r = int(input("Annual interest rate:"))
t = int(input("time:"))

si = (p*r*t)/100
print(si)

print("Amount :", p+si)
