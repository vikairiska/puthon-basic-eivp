"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    sq = []

    for n in numbers:
        power = n ** 2
        sq.append(power)

    return sq
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True
def filter_numbers(*numbers, filter = 'even'):
    if filter == 'even':
        return [x for x in numbers if x%2 == 0]
    elif filter == 'even':
        return [x for x in numbers if x%2 == 1]
    else:
        return [x for x in numbers if prime(x)]

numbers = [1,4,5,7,9,1,0,10,13,21]

even_num = filter_numbers(numbers, 'even')
odd_num = filter_numbers(numbers, 'odd')
prime_num = filter_numbers(numbers, 'prime')

print(even_num)
print(odd_num)
print(prime_num)
