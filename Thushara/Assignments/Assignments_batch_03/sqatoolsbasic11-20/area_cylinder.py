# Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
rad = int(input("Enter the radius:"))
h = int(input("Enter the height :"))

area = 2*3.14*rad*h + 2*3.14*rad*rad
print("Area of the cylinder :",area)
