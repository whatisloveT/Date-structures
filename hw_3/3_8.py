# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
number_list = []
for i in range(4):
    temp_list = []
    for j in range(4):
        temp_list.append(int(input('Введите значение : ')))
    temp_list.append(sum(temp_list))
    number_list.append(temp_list)
# Вывод матрицы
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j], end=' ')
    print('\n')
