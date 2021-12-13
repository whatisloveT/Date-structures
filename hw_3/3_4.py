# 4. Определить, какое число в массиве встречается чаще всего.
a = [1,1,22,2,2,2,3,4,5,5,6,6,6,7]

while len(a) !=0:
    b = tuple(set(a))
    for i in range(len(b)):
        a.remove(b[i])

print(a, b)