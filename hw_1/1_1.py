# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input('Введите трехзначное число :'))
if num < 100 or num > 999:
    print('Вы Ввели не трехзначное число, попробуте снова')
else:
    sum_num = num // 100 + (num%100)//10 + num%10
    multi_num = (num // 100) * ((num%100)//10) * (num%10)
    print(f'Сумма цифр числа = {sum_num} \nПроизведение цифр числа = {multi_num}')