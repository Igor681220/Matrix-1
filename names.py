import random
from random import shuffle

# вводим имена с заглавной или прописной буквы, разницы нет
# все равно выведется список с Заглавной буквы

print('Вводите имена игроков, не менее 6-ти, Enter')
print('для окончания ввода, просто нажмите Enter')

name_player = input().capitalize()
names = []
while name_player:
    try:
        names.append(name_player)
        name_player = input().capitalize()
    except:
        break
print(names)
print('\n')
# print([random.choice(names)])
# print('\n')

# выбор количества игроков

print('Введите количество игроков от 2-х до 6-ти, Enter')
player = int(input())
for player in names:
    if player == player:
        print("player: {player[0]}".format(player = [random.choice(names)]))
        names.remove(player)
        print(names)
        continue
    
