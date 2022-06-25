import copy

a = [1,2,3,4]
b = ["a","b",]

b.append(a[:])
print(id(b[2]))

c = copy.copy(b)
print(id(c[2]))


d = copy.deepcopy(b)
print(id(d[2]))