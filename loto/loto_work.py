import random
import copy
from Card import Create_cards as Cards


def strike(num, card):
    count = 0
    for i in card:
        if num in i:
            card[count][i.index(num)] = '-'
        count += 1
    return card


def check_nums_end(card):
    result = 0
    for i in card:
        for j in i:
            if type(j) == int:
                result = 1
    return result


player = Cards()[0]
comp = Cards()[0]
last_player = player[:]

barrels = [i for i in range(1, 91)]

while len(barrels) > 0:
    print('\n' * 100)
    if check_nums_end(player) == 0:
        print('Поздравляем. Вы выиграли.')
    current_bar = barrels.pop(random.randint(0, (len(barrels)) - 1))
    comp = strike(current_bar, comp)
    if check_nums_end(comp) == 1:
        print('Новый бочонок: {} (осталось {})\n'.format(current_bar, len(barrels)))
    else:
        print('Последний бочонок: {}. Компьютер выиграл'.format(current_bar))
        break

    print('------ Ваша карточка -----')
    for i in player:
        for some in i:
            print('{:<3}'.format(some), end='')
        print()
    print('-' * 26, '\n')

    print('-- Карточка компьютера ---')
    for i in comp:
        for some in i:
            print('{:<3}'.format(some), end='')
        print()
    print('-' * 26)
    if check_nums_end(player) == 0:
        break
    choice = input('Зачеркнуть цифру? (y/n)')
    last_player = copy.deepcopy(player)
    if choice == 'y':
        player = strike(current_bar, player)
        if last_player == player:
            print('Вы проиграли. В вашей карточке нет номера {}'.format(current_bar))
            break
        else:
            print('\n' * 100)
    elif choice == 'n':
        player = strike(current_bar, player)
        if last_player != player:
            print('Вы проиграли. В вашей карточке есть номер {}'.format(current_bar))
            break
        else:
            print('\n' * 100)
    else:
        print('Вы проиграли. Вы ввели {}, вместо y/n'.format(choice))
        break

