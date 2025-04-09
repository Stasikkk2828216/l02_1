import random
import datetime
import math

# Задача 1: Случайное число
random_number = random.randint(1, 100)
print(f"Случайное число: {random_number}")

# Задача 2: Текущая дата и время
now = datetime.datetime.now()
print(f"Текущая дата и время: {now}")

# Задача 3: Квадратный корень (с math и без)
number = float(input("Введите число: "))
print(f"Квадратный корень (math): {math.sqrt(number)}")

# Без math
def sqrt_without_math(n):
    return n ** 0.5
print(f"Квадратный корень (без math): {sqrt_without_math(number)}")
