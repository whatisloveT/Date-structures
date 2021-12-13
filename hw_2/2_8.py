# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
count_inp = int(input('Введите кол-во вводимых чисел : '))
search_num = int(input('Какую цифру проверяем? '))
number_list = []
count = 0
temp_num = 0
for i in range(count_inp):
    temp_elem = int(input('Введите число : '))
    number_list.append(temp_elem)
    for n in range(len(str(temp_elem))):
        if temp_elem%10 == search_num:
            count += 1
            temp_elem == temp_elem // 10
        else:
            temp_elem == temp_elem // 10

print(f'В последовательности чисел"{number_list}" цифра {search_num}, встречается {count} раз')