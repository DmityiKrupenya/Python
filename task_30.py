# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input('Введите значение первого элемента: ')) # первый элемент
d = int(input('Введите разность:')) # Разность
scale_el = int(input('Введите количество элементов в массиве: ')) #количество элементов

res = [first_el + (i - 1) * d for i in range(1, scale_el + 1)]
print(res)



