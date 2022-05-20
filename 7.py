d = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("Given Dictionary is:\n", d)
n = []
for k, v in d.items():        # k=keys & v = values
    n.append([k]+v)           # converting dict to list by using k & v
print("\nThe Converted list is:\n", n)