import random

def is_valid(num):
    if num.isdigit():
        return 0 < int(num) < 101
    return False

def is_equal(num):
    if num == x:
        print('Вы угадали, поздравляем!')
    elif num > x:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Ваше число меньше загаданного, попробуйте еще разок')

while True:
    print('Добро пожаловать в числовую угадайку. Сыграем?')
    enter = input('Введите "да" или "нет" \n')
    if enter == 'нет':
        print('Всего хорошего!')
        break
    else:
        x = random.randint(1, 100)
        while True:
            n = input('Введите число от 1 до 100 \n')
            while not is_valid(n):
                print('А может быть все-таки введем целое число от 1 до 100?')
                n = input('Введите число от 1 до 100 \n')
            n = int(n)
            is_equal(n)
