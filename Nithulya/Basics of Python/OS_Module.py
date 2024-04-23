
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
#     elif os.path.isfile(dataPath):        #  osPath.isfile - This will check given path is file.
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
import shutil
src_location = r"C:\PythonAutomation\Nithulya\second file.txt"
tar_location = r"C:\PythonAutomation\Nithulya\NewFolder\second file copy.txt"   # Copy of second file saved on NewFolder as second file copy.txt
shutil.copy(src_location, tar_location)