list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
print("The Original list is:")
print(list1)
list1[2][1][2].extend(list2)
print("After adding data is:")
print(list1)