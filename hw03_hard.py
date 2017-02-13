# Задание-1:
# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 2 5/6 + -5 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

def table(table_of_list):  # файл в списки, с удалением мусора
    table_of_list = [[j for j in table_of_list[i].split(' ')] for i in range(len(table_of_list))]
    for i in range(len(table_of_list)):
        while '' in table_of_list[i]:
            table_of_list[i].remove('')
        if '\n' in table_of_list[i][len(table_of_list[i]) - 1]:
            table_of_list[i][len(table_of_list[i]) - 1] = (table_of_list[i][len(table_of_list[i]) - 1])[:-1]
    return table_of_list

with open('data/workers', 'r', encoding='UTF-8') as file:
    list_of_workers = table(file.readlines())


with open('data/hours_of', 'r', encoding='UTF-8') as file:
    hours = table(file.readlines())
    hours[0][2] = hours[0][2] + ' ' + hours[0][3]  # чтобы не усложнять, склеиваем третий столбец с четвертым
    hours[0] = hours[0][:-1]

for i in range(len(list_of_workers)):  # Склеиваем два списка
    for j in range(len(hours)):
        if list_of_workers[i][0] == hours[j][0] and list_of_workers[i][1] == hours[j][1]:
            list_of_workers[i].append(hours[j][2])

list_of_workers[0].append('Сумма')  # Добавляем поле

for i in range(1, len(list_of_workers)):  # Считаем зарплаты, вписываем в "Сумму"
    a = list(list_of_workers[i])
    if int(a[4]) >= int(a[5]):
        a.append(str(int(int(a[2]) / int(a[4]) * int(a[5]))))
    else:
        a.append(str(int(int(a[2]) + (((int(a[5]) - int(a[4])) * (int(a[2]) / int(a[4]))) * 2))))
    list_of_workers[i] = a

max_len = 0  # Считаем ширину полей
for i in list_of_workers:
    for j in i:
        if len(j) > max_len:
            max_len = len(j)

# Создаем файл с обработанными данными
with open('data/salarys', 'w', encoding='UTF-8') as file:
    in_strings = []
    for i in list_of_workers:
        file.write(' '.join(['{:<{m}}'.format(i, m=max_len + 1) for i in i]) + '\n')

# Проверяем, что получилось
with open('data/salarys', 'r', encoding='UTF-8') as file:
    print(file.read())


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

