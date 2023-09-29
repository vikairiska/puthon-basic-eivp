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
def filter_numbers(numbers, filter_type):
    result = []
    for num in numbers:
        if filter_type == ODD and num % 2 == 1:
            result.append(num)
        elif filter_type == EVEN and num % 2 == 0:
            result.append(num)
        elif filter_type == PRIME and prime(num):
            result.append(num)
    return result

numbers = [1, 2, 3]
print(filter_numbers(numbers, ODD))
print(filter_numbers(numbers, EVEN))
print(filter_numbers(numbers, PRIME))
