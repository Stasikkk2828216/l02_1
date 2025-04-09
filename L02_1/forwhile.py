
# Задача 1: Числа от 1 до 10 (for)
for i in range(1, 11):
    print(i, end=' ')
print()

# Задача 2: Числа от 1 до N
n = int(input("Введите N: "))
for i in range(1, n + 1):
    print(i, end=' ')
print()

# Задача 3: Сумма чисел от 1 до 100 (while)
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"Сумма: {total}")
