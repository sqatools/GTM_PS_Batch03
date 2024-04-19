# Arithmetic Operators
print(10 + 20)
print(20 - 10)
print(10 * 2)
print(10 ** 2)  # exponential
print(10 ** 2 ** 2)  # exponential - Right to left
print((10 ** 2) ** 3)  # exponential - Here Parenthesis is calculated first
print(10 / 3)  # Float division - then it will provide output in float
print(10 // 3)  # Floor division - then it will provide output in float
print(10 % 3)  # Remainder

# Relational Operators
print(2 == 3)
print(2 != 3)
print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)

# order of operators -> Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
print(5 + 15 * 20 - 2 / 6 ** 3 - (3 + 1))
print(3 + 1)
print(6 ** 3)
print(15 * 20)
print(5 + 300 - 2 / 216 - 4)
print(2 / 216)
print(5 + 300 - 0 - 4)
print(305 - 0 - 4)

# (a+b)^2  =a^2 + b^2 + 2ab
a = 4
b = 7
lhs = (a + b) ** 2
print("lhs result :", lhs)
rhs = a ** 2 + b ** 2 + 2 * a * b
print("rhs result:", rhs)

# converting Km to miles. miles = km * 0.621371
km = int(input('Enter Km value'))
miles = km * 0.621371
print(miles)
