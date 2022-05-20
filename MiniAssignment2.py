from collections import Counter
class DuplicateValues:
    def DuplicateValues(self, n):
        k = []
        v = []
        for i in range(len(n)):
            res = Counter(n[i])
            for j in range(len(list(res.values()))):
                if ((list(res.values()))[j]) > 1:
                    k.append((list(res.keys()))[j])
                    v.append((list(res.values()))[j])
        for i in range(len(k)):
            print(k[i], "->", v[i])


n = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
print("The list is:")
print(n)
print("\nThe duplicate values:")
duplicate = DuplicateValues()
duplicate.DuplicateValues(n)


