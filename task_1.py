# 1. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_num = int(input('Введите первое число прогрессии: '))
step = int(input('Введите шаг прогрессии: '))
amount = int(input('Введите количество элементов прогрессии: '))

def arithmetic_progress(first_elem, div, amount_elem):
    array_num = [first_elem]
    next_elem = first_elem
    for i in range(amount_elem):
        next_elem += div
        array_num.append(next_elem)
    return array_num

print(arithmetic_progress(first_num, step, amount))