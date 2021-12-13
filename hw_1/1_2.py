# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.
num_one = int(bin(5)[2:])
num_two = int(bin(6)[2:])
and_bin = num_one | num_two # И работает по правилу 1 и 1 = 1, 1 и 0 = 0
or_bin = num_one & num_two # ИЛИ работает по правилу 1 или 1 = 0, 1 или 0 = 1, 0 или 0 = 0
not_or = num_one ^ num_two  # Исключающие ИЛИ 1 ^ 0 = 1 , 0 ^ 1 = 1 , 1 ^ 1 = 0, 0 ^ 0 = 0
left_bin = 5 << 2  # Сдвиг вправо умножает целую часть числа два раза на 2 5*2 = 10 , 10*2 = 20
right_bin = 5 >> 2   # Сдвиг вправо делит целую часть числа два раза на 2. 5/2 = 2.5 , 2/2= 1
print(f'Число 5 в двоичной системе : {num_one} \nЧисло 6 в двоичной системе : {num_two}\n'
      f'Результат операции "И" : {and_bin}\nРезультат операции "ИЛИ" : {or_bin}\n'
      f'Результат операции "ИСКЛЮЧАЮЩИЕ ИЛИ" : {not_or}\n'
      f'Результат сдвига числа 5 влево : {left_bin}\n'
      f'Результат сдвига числа 5 вправо : {right_bin}')