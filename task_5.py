print('Задача 5. Текстовый редактор')


# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, digit, letter):
    count_digit, count_letter = 0, 0
    text_lower = text.lower()
    letter_lower = letter.lower()
    for simbol in text_lower:
        if simbol == letter_lower:
            count_letter += 1
        elif simbol == digit:
            count_digit += 1

    print()
    print(f'Количество цифр {digit}: {count_digit}')
    print(f'Количество букв {letter}: {count_letter}')


def main():
    text = input('Введите текст: ')
    digit = input('Какую цифру ищем? ')
    letter = input('Какую букву ищём?: ')
    count_letters(text, digit, letter)


main()
