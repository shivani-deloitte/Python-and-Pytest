list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        res = i+ " "+j
        list3.append(res)
print(list3)