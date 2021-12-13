# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем
# за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

n = 1
hid_num = random.randint(0, 100)
while n < 11:
    print(f'Попытка № {n}')
    num = int(input('Введите число : '))
    if num > hid_num:
        print('Загаданное число меньше!')
    elif num < hid_num:
        print('Загаданное число больше!')
    else:
        print('Вы угадали')
        break
    n += 1


print(f'Загаданное число {hid_num}')
