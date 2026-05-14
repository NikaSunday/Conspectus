import random

def is_valid(num):
    if num.isdigit():
        return 0 < int(num) < 101
    return False

def is_equal(num, target):
    if num == target:
        print('Вы угадали, поздравляем!')
        return True
    elif num > target:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return False
    else:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return False

def play_game(target):
    while True:
        n = input('Введите число от 1 до 100 \n')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if is_equal(int(n), target):
            return True


print('Добро пожаловать в числовую угадайку. Сыграем?')
game_finish = False

while not game_finish:
    enter = input('Введите "да" или "нет" \n')
    if enter == 'нет':
        print('Всего хорошего!')
        game_finish = True
    else:
        x = random.randint(1, 100)
        play_game(x)
        print('Продолжим?')
