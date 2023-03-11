# 2. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random
array = []
min_value = int(input('Введите начальное значение диапазона: '))
max_value = int(input('Введите конечное значение диапазона: '))

for i in range(20):
    array.append(random.randint(-10,10))

print(array)

def return_indexes_elements_range(start_range, end_range, source_array):
    arr_indexes = []
    for i in range(len(source_array)):
        if start_range < source_array[i] < end_range:
            arr_indexes.append(i)
    return arr_indexes

output_array = return_indexes_elements_range(min_value, max_value, array)
print(output_array)