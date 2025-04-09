
# Задача 1: Информация о студенте
student = {
    "name": "Иван",
    "age": 20,
    "course": 3
}
print(student)

# Задача 2: Объединение словарей
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Задача 3: Проверка наличия ключа
key = input("Введите ключ для проверки: ")
print(f"Ключ '{key}' есть в словаре: {key in student}")
