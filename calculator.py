# Функция для сложения
def add(x, y):
    return x + y

# Функция для вычитания
def subtract(x, y):
    return x - y

# Функция для умножения
def multiply(x, y):
    return x * y

# Функция для деления
def divide(x, y):
    return x / y
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Запрашиваем у пользователя выбор операции
choice = input("Введите номер операции (1/2/3/4): ")

# Запрашиваем у пользователя ввести два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print("Результат сложения:", add(num1, num2))
elif choice == '2':
    print("Результат вычитания:", subtract(num1, num2))
elif choice == '3':
    print("Результат умножения:", multiply(num1, num2))
elif choice == '4':
    print("Результат деления:", divide(num1, num2))
else:
    print("Неверный выбор операции")
