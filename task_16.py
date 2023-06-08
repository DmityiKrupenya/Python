# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Enter the number of elements in the array: '))

a = [int(input('enter array element: ')) for i in range(n)]
print(a)

x = int(input('Enter the number you want to quantify in the array: '))
sum = 0
for i in range(len(a)):
    if a[i] == x:
        sum = sum + 1

print(sum)
    