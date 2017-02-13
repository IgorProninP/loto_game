# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1

from random import randint

def fibonacci(n, m):
    count, last, next = 1, 0, 1 # если я все же понял неправильно и ряд сдвигается на единицу, то last = 1
    while count != n:
        print(count, next)
        count += 1
        last, next = next, next + last

fibonacci(randint(1, 10), randint(10, 20))

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()


def sort_to_max(origin_list):
    count = 1
    while count < len(origin_list):
        for i in range(len(origin_list) - count):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        count += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter

def any(x):
    if 4 == x:
        return True
    else:
        return False

def my_filter(func, params):
    params = [i for i in params]
    out = []
    for i in range(len(params)):
        temp = list(map(func, params))
    for i in range(len(params)):
        if temp[i]:
            out.append(params[i])
    return out

var = (1, 4, 2, 6)
print(list(my_filter(any, var)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

from random import randint

x1, y1, x2, y2, x3, y3, x4, y4 = (randint(1, 20) for i in range(8))
if (x2 - x1) == (x4 - x3) and (y2 - y1) == (y4 - y3):
    print('True')
else:
    print('False')
