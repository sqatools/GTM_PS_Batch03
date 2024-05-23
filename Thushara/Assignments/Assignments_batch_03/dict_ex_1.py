st1 = "ProGraM"
st2 = st1.lower()
list1 = [1, 2, 3, 4, 5, 6, 7]
dict1={}
for i in range(len(st1)):
    dict1[st2[i]*(i+1)]= i+1
print(dict1) #{'p': 1, 'rr': 2, 'ooo': 3, 'gggg': 4, 'rrrrr': 5, 'aaaaaa': 6, 'mmmmmmm': 7}
