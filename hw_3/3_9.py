# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы
import random
n = 5
m = 7
array_el = []
min_list = [0]*m
for i in range(n):
    temp_list = []
    for j in range(m):
        temp_list.append(random.randint(-100,100))
        if min_list[j] > temp_list[j]:
            min_list[j] = temp_list[j]
        print(temp_list[j], end=' ')
    print('\n')
    array_el.append(temp_list)

print(max(min_list))