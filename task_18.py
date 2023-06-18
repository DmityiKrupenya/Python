# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Enter the number of elements in the array: '))
a = [int(input('enter array element: ')) for i in range(n)]
print(a)

x = int(input('Enter a number to find the closest value in the array: '))
sum = 0
for i in range(len(a)):
    if i == x:
        print('В массиве есть искомое число!')
        break
    else:
        m = min(a, key=lambda i: abs(i - x))
print(f"Близкий по величине элемент {m} ")

