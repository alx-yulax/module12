print('Задача 4. Число наоборот')


# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
#
# Введите число: 1000
# Число наоборот: 0001
#
# Введите число: 0
# Программа завершена!
#
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
#
# Введите число: 1230
# Число наоборот: 321
#
# Кстати, нули, которые мы убрали, называются ведущими.

def print_reverse(number):
    reverse_number = ''
    while number > 0:
        digit = number % 10
        reverse_number += str(digit)
        number //= 10
    print('Число наоборот:', reverse_number)
    main()


def main():
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
    else:
        print_reverse(number)


main()
