print('Задача 3. Апгрейд калькулятора')


# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def summ_digits(number):
    temp_number = number
    summ = 0
    while temp_number > 0:
        summ += temp_number % 10
        temp_number //= 10
    print(f'Сумма цифр числа {number} = {summ}')
    calculate()


def max_digits(number):
    temp_number = number
    maximum = temp_number % 10
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if digit > maximum:
            maximum = digit
    print(f'Максимальная цифра числа {number} = {maximum}')
    calculate()


def min_digits(number):
    temp_number = number
    minimum = temp_number % 10
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if digit < minimum:
            minimum = digit
    print(f'Минимальная цифра числа {number} = {minimum}')
    calculate()


def calculate():
    number = int(input('Введите число: '))
    print('Введите действие')
    action = int(input('0 - выход из программы, 1- вывести сумму цифр, 2- максимальную, 3- минимальную цифру: '))
    if action == 1:
        summ_digits(number)
    elif action == 2:
        max_digits(number)
    elif action == 3:
        min_digits(number)
    elif action == 0:
        print('Спасибо, что воспользовались приложением.')
    else:
        print('Не верное действие, начем сначала.')
        calculate()


calculate()
