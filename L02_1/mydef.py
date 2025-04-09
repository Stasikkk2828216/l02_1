# Задача 1: Сумма двух чисел
def add(a, b):
    return a + b

# Задача 2: Проверка на простое число
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Задача 3: Среднее значение списка
def average(numbers):
    return sum(numbers) / len(numbers)
    