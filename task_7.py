import random

print('Задача 7. Недоделка')


# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)

    user_choice = int(input('Выберите 1- камень, 2- ножницы или 3- бумагу: '))

    if user_choice < 1 or user_choice > 3:
        print('Неверный ввод! Попробуйте снова.')
        rock_paper_scissors()

    print(f'Компьютер выбрал: {computer_choice}')

    if user_choice == computer_choice:
        print('Ничья!')
    elif (user_choice == 1 and computer_choice == 'ножницы') or \
            (user_choice == 2 and computer_choice == 'бумага') or \
            (user_choice == 3 and computer_choice == 'камень'):
        print('Вы победили!')
    else:
        print('Вы проиграли!')
    main_menu()


def guess_the_number():
    number = random.randint(1, 100)
    guess = None

    print('Игра "Угадай число": Я загадал число от 1 до 100. Попробуйте его угадать!')

    while guess != number:
        guess = int(input('Введите ваше предположение: '))

        if guess < number:
            print('Загаданное число больше.')
        elif guess > number:
            print('Загаданное число меньше.')
        else:
            print(f'Поздравляю! Вы угадали число {number}!')

    main_menu()


def main_menu():
    print('\nГлавное меню:')
    print('1 - Игра "Камень, ножницы, бумага"')
    print('2 - Игра "Угадай число"')
    print('0 - Выход')

    choice = int(input('Выберите игру (1, 2) или выход (0): '))

    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    elif choice == 0:
        print('Выход из программы.')
    else:
        print('Неверный выбор. Попробуйте снова.')
        main_menu()


main_menu()
