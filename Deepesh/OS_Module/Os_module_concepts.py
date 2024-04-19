import os
import shutil

# get current working directory path

cur_path = os.getcwd()
print("cur path :", cur_path)
# E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Deepesh\OS_Module

# Change working directory path


#os.chdir(r"E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok")
#print(os.getcwd())
# E:\Trainings\GTM_PS_Batch03_8March2024\GTM_PS_Batch03\Ashok


#Get list of all files and folder from target location
tar_path = r"E:\Filesdata"
file_folder_list = os.listdir(tar_path) # This will provide list of all files and folder
print(file_folder_list)

# join path with os.path.join()
for data in file_folder_list:
    print(data)
    data_path = os.path.join(tar_path, data) # This will join two paths
    print(data_path)

    # os.path.isfile # This will check given path is file
    # os.path.isdir # this will check the given path is directory or not
    if os.path.isdir(data_path):
        print("Folder")
    elif os.path.isfile(data_path):
        print("File")

    print("_"*40)



################ CHeck if the path is file or not ################

print(os.path.isfile(r"E:\Filesdata\count_name.txt")) #True

# check given location exist or not
result1 = os.path.exists(r"E:\Filesdata\count_name.txt") # True
print("File exist or not :", result1)
result2 = os.path.exists(r"E:\Filesdata\count_name123.txt") # False
print("File exist or not :", result2)

##################################################################
# create directory or current location
# os.mkdir("folder1")

# create directory on target location:
# os.mkdir(r"E:\Filesdata\GTM_BATCH4")

# create multi level folder directory
# os.makedirs(r"E:\Filesdata\GTM_BATCH4\f1\f2\f3")

# Remove empty directory
# os.rmdir(r"E:\Filesdata\GTM_BATCH3")

# Remove non empty directory
# os.removedirs(r"E:\Filesdata\GTM_BATCH4")

# Remove non empty directory
# shutil.rmtree(r"E:\Filesdata\GTM_BATCH4")

# copy files from one location to another location
src_location = r"E:\Filesdata\file1.txt"
tar_location = r"E:\Filesdata\Tavet\file1_batch2_copy.txt"
shutil.copy(src_location, tar_location)


