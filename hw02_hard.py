# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

print('УРАВНЕНИЕ:\n', '-' * 10)

a = [str(i) for i in equation.split()]
a[2] = a[2].replace('x', '')
y = int(a[2]) * x + float(a[4])
print(y, '\n' + '-' * 10,'\n')


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена
# дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от
# месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня,
# 2- месяц, 4 -год)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


def check(ch):
    try:
        arr = [str(i) for i in ch.split('.')]
        return True
    except IndexError:
        return False


def check_1(ch1):
    arr = [str(i) for i in ch1.split('.')]
    if len(arr[0]) != 2 or len(arr[1]) != 2 or len(arr[2]) != 4:
        return False
    elif len(arr[0]) < 1 or len(arr[1]) < 1 or len(arr[2]) < 1:
        return False
    elif int(arr[0]) > 31 or int(arr[1]) > 12 or int(arr[2]) > 9999:
        return False
    elif int(arr[1]) < 8 and (int(arr[1]) % 2) == 0 and int(arr[0]) > 30:
        return False
    elif int(arr[1]) > 8 and (int(arr[1]) % 2) != 0 and int(arr[0]) > 30:
        return False
    elif int(arr[2]) % 4 == 0 and int(arr[2]) % 100 != 0 or int(arr[2]) % 400 == 0:
        if int(arr[1]) == 2 and int(arr[0]) > 29:
            return False
        else:
            return True
    elif int(arr[1]) == 2 and int(arr[0]) > 28:
        return False
    else:
        return True

print('ДАТА:\n' + '-' * 10)
signal = 0
while signal == 0:
    a = input('Введите дату (dd.mm.yyyy):')
    if not check(a) or not check_1(a):
        print('Введен некорректный символ, или неверный формат!\n')
        continue
    print('\nВсе отлично, проверка пройдена.'.upper())
    signal = 1
print('-' * 10,'\n')


# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую
# бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три
# комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты
# определять, на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

from random import randint
from math import sqrt

print('БАШНЯ:\n' + '-' * 10)
N = randint(1, 2000000000)

# Чтобы не усложнять, проверим 1
if N == 1:
    print("Номер комнаты: 1, Номер этажа: 1, Порядковый номер: 1")
    exit()

# Ищем этаж
count = 0
block = 1
floor = 1
while count < N:
    count += block * block
    if count < N:
        block += 1
        floor += block
floor -= (count - N) // block

# Ищем номер на этаже
num_of_begin = count - (((count - N) // block) * block) - block + 1
whole_floor = [int(i) for i in range(num_of_begin, num_of_begin + block)]
num_in_floor = whole_floor.index(N) + 1

print("Номер комнаты:", N, "Номер этажа:", floor, "Порядковый номер:",
      num_in_floor,'\n' + '-' * 10,'\n')
