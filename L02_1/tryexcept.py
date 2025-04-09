# Задача 1: Обработка ввода числа
try:
    num = int(input("Введите число: "))
    print(f"Вы ввели: {num}")
except ValueError:
    print("Ошибка: введите корректное число")

# Задача 2: Обработка отсутствия файла
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Ошибка: файл не найден")

    