def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль невозможно"
    return x / y

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4) или 'q' для выхода: ")

        if choice == 'q':
            print("Завершение работы калькулятора.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите числовое значение.")
                continue

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Ошибка: выберите корректную операцию.")

calculator()
