import csv


# CSV reader gives the list values
# Dict reader give the dict format values

# 1st way of reading the csv file without using csv module.
#
def read_csv_file1(filename):
    csvfile = open(filename, 'r')
    reading = csvfile.read()
    print(reading)


read_csv_file1("emp_file.csv")


#
def read_csv_file2(filename):
    with open(filename, 'r') as f1:
        csvfile1 = f1.read()
        print(csvfile1)


read_csv_file2("emp_file.csv")

# 2nd way of reading CSV files using csv module
"""
The csv module includes a reader() method that can be used for read a csv file into our program. The
reader function converts each line of a specified line into a list of columns. Then the python's
built-in open() function, which returns a file object, is used to open the CSV file as text file.
"""


def read_csv_file3(filename):
    f = open(filename, 'r')
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)


read_csv_file3("emp_file.csv")


#
def read_csv_file4(filename):
    f = open(filename, 'r')
    csv_reader = csv.reader(f)
    next(csv_reader)  # next() function is used to get the next item from a collection of values.
    for row in csv_reader:
        print(row)


read_csv_file4("emp_file.csv")


# to find the min and max sal of employees

# def read_csv_file4(filename):
#     f2 = open(filename, 'r')
#     csv_reader = csv.reader(f2)
#
#     sals = []
#     for row in csv_reader:
#         sals.append((row[2]))
#
#     print(sals)
#     print("Min value is:", min(sals))
#     print("Max value is:", max(sals))
#
#
# read_csv_file4("emp_file.csv")

# DictReader # - We can read the csv data in form of dictionary format as well.

def read_csv_file5(filename):
    with open(filename, 'r') as f5:
        dict_reader = csv.DictReader(f5)
        for row in dict_reader:
            print(row)


read_csv_file5("emp_file.csv")

covid = [('Country', 'Doses', 'People', 'Percentage'),
         ('India', '186Cr', '84.1Cr', 61),
         ('Australia', '184Cr', '82.1Cr', 60),
         ('US', '284Cr', '92.1Cr', 82)]


def write_csv_file1(filename):
    with open(filename, 'w', newline='') as f6:
        csv_writer = csv.writer(f6)
        for t in covid:
            csv_writer.writerow(t)

        f6.close()


write_csv_file1("Book3.csv")


def write_csv_file2(filename):
    with open(filename, 'w', newline='') as f7:
        fields = ['Country', 'Doses', 'People', 'Percentage']
        csv_writer = csv.DictWriter(f7, fields)
        csv_writer.writeheader()

        for d in covid:
            csv_writer.writerow(d)

        f7.close()


write_csv_file1("Book4.csv")
