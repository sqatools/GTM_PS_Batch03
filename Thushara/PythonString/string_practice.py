# Practice Assignment

# replace first char with last char
str1 = "IPL 2024 Cricket Trophy"
fist_char = str1[0]
last_char = str1[-1]
remaining_part = str1[1:-1]
# result = f"{last_char}{remaining_part}{fist_char}"
result = f"{str1[-1]}{str1[1:-1]}{str1[0]}"
print("Result :", result)  # yPL 2024 Cricket TrophI

str1 = "String formatting"
result = f"{str1[-1]}{str1[1:-1]}{str1[0]}"

print(result) #gtring formattinS


# question2:  Repeat every second character 2 times in the given string
str1 = "python"
# output = "pyythhonn"
result = f"{str1[0]}{str1[1]*2}{str1[2]}{str1[3]*2}{str1[4]}{str1[-1]*2}"
print(result) #pyythhonn

# question3 :
str2 = "Good Morning"
# output = "ggninroM dooGG"
result = f"{str2[-1]*2}{str2[-2:0:-1]}{str2[0]*2}"
print(result)
