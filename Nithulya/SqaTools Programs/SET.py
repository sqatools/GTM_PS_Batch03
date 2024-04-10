#1. Python program to find common elements in three lists using sets.a = [1, 5, 10, 20, 40, 80],b = [6, 7, 20, 80, 100],
#c = [3, 4, 15, 20, 30, 70, 80, 120]
# a = [1, 5, 10, 20, 40, 80]
# b = [6, 7, 20, 80, 100]
# c = [3, 4, 15, 20, 30, 70, 80, 120]
# set1=set(a)
# set2=set(b)
# set3=set(c)
# s1=set1.intersection(set2)
# print('S1 & S2:',s1)                         # S1 & S2: {80, 20}
# common_element=s1.intersection(set3)
# print('Common_element:',common_element)      # Common_element: {80, 20}
# final_list=list(common_element)
# print('Final list:',final_list)              # Final list: [80, 20]

#2.Add a list of elements to a set.sample_set = {"Yellow", "Orange", "Black"},sample_list = ["Blue", "Green", "Red"]
# set1 = {"Yellow", "Orange", "Black"}
# list1 = ["Blue", "Green", "Red"]
# set1.update(list1)
# print('Updated set1:',set1)        # Updated set1: {'Blue', 'Red', 'Green', 'Yellow', 'Black', 'Orange'}

#3.Update the first set with items that don’t exist in the second set.set1 = {10, 20, 30},set2 = {20, 40, 50}
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print('Set1:',set1)                  # Set1: {10, 30}

#4.Write a Python program to remove items 10, 20, 30 from the following set at once.set1={10, 20, 30, 40, 50},Output:{40, 50}
# set1={10, 20, 30, 40, 50}
# set1.difference_update({10,20,30})
# print('Updated set1:',set1)              # Updated set1: {50, 40}

#5.Return a set of elements present in Set A or B, but not both. set1 = {10, 20, 30, 40, 50},set2 = {30, 40, 50, 60, 70}
#Output:{20, 70, 10, 60}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
output=set1.symmetric_difference(set2)
print('Output:',output)                     # Output: {20, 70, 10, 60}
