# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
y1 = int(input('Введите значение у первой точки : '))
x1 = int(input('Введите значение x первой точки : '))
y2 = int(input('Введите значение у второй точки : '))
x2 = int(input('Введите значение x второй точки : '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f'Уравнение имеет вид y={k}х+{b}')
