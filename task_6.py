print('Задача 6. НОД')


# Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Пример использования функции
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

result = gcd(number_1, number_2)
print(f'Наибольший общий делитель {number_1} и {number_2} = {result}')
