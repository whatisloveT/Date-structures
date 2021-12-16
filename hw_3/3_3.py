# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
array_el = []
len_p = int(input('Введите длину массива : '))
min = float('inf')
max = float('-inf')
ind_min = 0
ind_max = 0
for i in range(len_p):
    array_el.append(random.randint(-100,100))
    if array_el[i] < min:
        min= array_el[i]
        ind_min = i
    if array_el[i] > max:
        max = array_el[i]
        ind_max = i
print(array_el)
array_el[ind_max] = min
array_el[ind_min] = max
print(array_el)
print(min, max, ind_min, ind_max)