# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math

def my_round(number, ndigits):
    dot = 0
    if '.' in number:
        dot = number.index('.')  # Индекс запятой
        difference = len(number) - (dot + 1)  # Количество элементов за запятой
        if difference < ndigits:  # В случае, если знаков за запятой меньше, чем нужно округлить
            temp = ndigits - (len(number) - (dot + 1))
            return number + '0' * temp  # Дописываем нули
        elif difference == ndigits:  # Если знаков за запятой равно количству знаков для округления
            return number
        else:
            # return f'{float(number):.{ndigits}f}'
            # если format тоже нельзя, то конструируем велосипед:
            number_as_list = [i for i in number]  # Переводим число в список
            number_as_list.remove('.')  # Убираем запятую
            # Округление:
            for i in range(len(number_as_list) - 1, (dot + ndigits) - 1, -1):
                if int(number_as_list[i]) == 9:             # Проверяем наличие 9-ки
                    if int(number_as_list[i - 1]) == 9:     # Проверяем наличие 9-ки в предыдущей цифре
                        while int(number_as_list[i]) == 9:  # Ждем, пока не кончится ряд из 9-ок
                            number_as_list[i] = '0'         # Меняем девятку на 0
                            i -= 1                          # Счетчик
                        number_as_list[i] = str(int(number_as_list[i]) + 1)  # 9 кончились, добавляем 1 к следующему числу
                        if i < 0:  # Если вдруг все цифры 9
                            number_as_list.insert(0, '1')
                            dot += 1
                    else:                                   # Если 9-ка одна
                        number_as_list[i] = '0'
                        number_as_list[i - 1] = str(int(number_as_list) + 1)
                else:                                       # Если цифра не 9
                    # Если следующая цифра 9, а текущая > 5:
                    if int(number_as_list[i]) >= 5 and int(number_as_list[i - 1]) == 9:
                        i -= 1
                        if int(number_as_list[i - 1]) == 9:  # Проверяем наличие 9-ки в предыдущей цифре
                            while int(number_as_list[i]) == 9:  # Ждем, пока не кончится ряд из 9-ок
                                number_as_list[i] = '0'  # Меняем девятку на 0
                                i -= 1  # Счетчик
                            number_as_list[i] = str(int(number_as_list[i]) + 1)  # 9 кончились, добавляем 1 к следующему числу
                            if i < 0:
                                number_as_list.insert(0, '1')
                                dot += 1
                        else:  # Если 9-ка одна
                            number_as_list[i] = '0'
                            number_as_list[i - 1] = str(int(number_as_list) + 1)
                    elif int(number_as_list[i]) >= 5:
                        number_as_list[i - 1] = str(int(number_as_list[i - 1]) + 1)
            number_as_list.insert(dot, '.')
            number = ''.join(number_as_list)
            number = number[:(dot + ndigits) + 1]
            return number
    else:
        return f'{float(number):.{ndigits}f}'

print(my_round(str(input('Введите число ')), int(input('Введите кол-во знаков '))))

# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить

from random import randint

def lucky_ticket(ticket_number):
    if sum(ticket_number[:3]) == sum(ticket_number[-3:]):
        return True

if lucky_ticket(tuple(int(randint(0, 9)) for i in range(6))):
    print('Билет счастливый')
else:
    print('Билет несчастливый')
