
################ Get current working directory path #################################################
# import os
# curPath = os.getcwd()
# print("Current Path :", curPath)         # Current Path : C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python


############### Change working directory path ########################################################
# import os
# curPath = os.getcwd()
# os.chdir(r"E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok")
# print(os.getcwd())                          # E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok


############# Get list of all files and folder from target location ####################################
# import os
# tarPath = 'C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python'
# fileFolderList = os.listdir(tarPath)        # This will provide list of all files and folder
# print(fileFolderList)

############ join path with os.path.join() ############################################################
# import os
# tarPath = 'C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python'
# fileFolderList = os.listdir(tarPath)
# for data in fileFolderList:
#     dataPath = os.path.join(tarPath, data)              # This will join two paths
#     print(dataPath)
#     if os.path.isdir(dataPath):           # osPath.isdir - This will check whether the given path is directory or not
#         print("Folder")
#     elif os.path.isfile(dataPath):        #  osPath.isfile - This will check whether the given path is file.
#         print("File")


################ Check if the path is file or not ####################################################
# import os
# print(os.path.isfile(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\Data types.py"))         # True


################ Check given location exist or not #####################################################
# import os
# result1 = os.path.exists(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\Reverse.py")
# print("File exist or not :", result1)               # File exist or not : True

# result2 = os.path.exists(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\reversed.py")
# print("File exist or not :", result2)                 # File exist or not : False


############### Create directory on current location  ###################################################
# import os
# os.mkdir("folder1")                  # Created folder1 dir on current location


############## Create directory on target location  ####################################################
# import os
# os.mkdir(r"C:\\PythonAutomation\\Nithulya\\Folder1")        # Created Folder1


############ Create multi level folder directory  ######################################################
# import os
# os.makedirs(r"C:\\PythonAutomation\\Nithulya\\Folder1\\f1\\f2\\f3")  # Created f1,f2,f3


############# Remove empty directory  ##################################################################
# import os
# os.rmdir(r"C:\\PythonAutomation\\Nithulya\\Folder1\\f1\\f2\\f3")       # Removed f3


############ Remove non empty directory  ##############################################################
# import shutil
# shutil.rmtree(r"C:\\PythonAutomation\\Nithulya\\Folder1")          # Removed all folders including Folder1


############ Copy files from one location to another location  ############################################
# import shutil
# src_location = r"C:\PythonAutomation\Nithulya\second file.txt"
# tar_location = r"C:\PythonAutomation\Nithulya\NewFolder\second file copy.txt"   # Copy of second file saved on NewFolder as second file copy.txt
# shutil.copy(src_location, tar_location)


############ Get value from environment variable ###########################################################
import os
# val= os.getenv("Browser1")
# print("value :", val)

# path = os.getenv("Path")
# print("Path value :", path)

# chrome_path = os.getenv("CHROME_PATH")
# print("chromepath :", chrome_path)


############ Get size of file ##############################################################################
# import os
# filesize = os.path.getsize(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\ExcelFileHandling\SqlData.xlsx")
# print("File size :", filesize)       # File size : 6259


########### Get CPU count ##################################################################################
# import os
# cpu_count = os.cpu_count()
# print("CPU count of system :", cpu_count)        # CPU count of system : 8


############ Get mtime of the file ######################################################################
# import os
# mtime = os.path.getmtime(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\ExcelFileHandling\SqlData.xlsx")
# print("mtime :", mtime)            # mtime : 1713764810.704432


########### Run windows command #############################################################################
# import os
# os.system("control")                 # Open control panel of windows
#
# os.system("appwiz.cpl")              # Open program feature
#
# os.system("dir C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\ExcelFileHandling")        # Get all file folder data


############### Execute the python file using os module #########################################################
# import os
# os.system("python C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\ExcelFileHandling\ExcelFile.py")


############ Check file permission #######################################################################
"""
mode	Required.
os.F_OK: Checks if the path exists.
os.R_OK: Checks if the path is readable.
os.W_OK: Checks if the path is writable.
os.X_OK: Checks if the path is executable.
"""
# import os
# permission = os.access(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\Basics of Python\FileHandling\hello.txt", os.R_OK)
# print("File Permission :", permission)


#################### Generate random string in python ###################################################
# import os
# import random
# output = os.urandom(5)
# print("Random String :", output)     # b'\xae\x02F\xc54'


#################### Generate random integer ##############################################################

#1). It will return any random numbers in given values
# import random
# result = random.randint(10, 20)
# print('Random Value : ',result)            # Random Value :  13

#2). Return any random value in given range along with difference value as like range method.
# import random
# val = random.randrange(2, 10, 2)
# print('Random Value : ', val)                 # Random Value :  4

#3). It will provide random floating number 0 to 1
# import random
# val = random.random()
# print("Random floating value : ",val)            # Random floating value :  0.21560517257780343


#4). It will generate random binary numbers
# import random
# bin = ''
# for i in range(5):
#     val = random.randint(0, 1)
#     bin = bin + str(val)
# print('Binary random value : ',bin)               # Binary random value :  10010


#5).
# import random
# number = random.getrandbits(10)
# print(number, format(number, "0b"))                # 835 1101000011


########################################## Faker ############################################################
# import sqlite3
# from faker import Faker
# """
# pip install faker
# """
# fk = Faker()
#
# def initial_connection(db_file='students.db'):
#     con = sqlite3.connect(db_file)
#     return con
#
# def execute_query(query):
#     con = initial_connection()
#     con.execute(query)
#     print("table created successfully")
#     con.close()
#
# def insert_query(query):
#     con = initial_connection()
#     con.execute(query)
#     print("data inserted successfully")
#     con.commit()
#     con.close()

# def select_query(query):
#     con = initial_connection()
#     data = con.execute(query)
#     #con.close()
#     return data

# create_table = """create table studentinfo(firstname text, lastname text, email text, phone int)
# """

# print(dir(fk))
# for i in range(50):
#     f_name = fk.first_name()
#     l_name = fk.last_name()
#     email =  fk.email()
#     phone =  8768878644
#     print(f_name, l_name, email, phone)
#     insert_query_cmd = f"""insert into studentinfo(firstname, lastname, email, phone) values
#     ('{f_name}', '{l_name}', '{email}', {phone})
#     """
#     #execute_query(create_table)
#     insert_query(insert_query_cmd)

# select_query_details = """select * from studentinfo where firstname='Jason'"""
#
# data = select_query(select_query_details)
# for val in data:
#     print(val)

# from faker import Faker
# fake = Faker()
#
# print(fake.name())

