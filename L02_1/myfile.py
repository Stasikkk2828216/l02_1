# Задача 1: Создание файла и запись строки
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# Задача 2: Чтение файла
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Задача 3: Добавление строки в файл
with open("example.txt", "a") as file:
    file.write("\nНовая строка")
    