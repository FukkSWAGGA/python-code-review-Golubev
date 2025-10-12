def ADD(x,y):  # Нарушение PEP 8: имя функции в верхнем регистре, отсутствуют пробелы после запятой
    return x + y


def Subtract(a, b):  # Нарушение PEP 8: имя функции должно быть в нижнем регистре
    return a - b


def multiply(a, b):
    result = a * b   # Избыточная переменная, нарушен принцип KISS
    return result


def divide(a, b):
    return a / b     # Нет проверки делителя на ноль


def main():
    print("Калькулятор!")  
    print("Введите выражение в формате: число операция число")

    while True:
        userInput = input(">>> ")   # Нарушен стиль именования переменных (camelCase вместо snake_case)
        if userInput == "exit":     # Нет приведения к нижнему регистру, 'EXIT' не сработает
            break

        parts = userInput.split()
        if len(parts) != 3:
            print("Ошибка: используйте формат 'a + b'")
            continue

        a = parts[0]    # Нет преобразования типов, значения остаются строками
        op = parts[1]
        b = parts[2]

        if op == "+":
            print(ADD(a,b))   # Отсутствуют пробелы после запятых, передаются строки, будет конкатенация
        elif op == "-":
            print(Subtract(a,b))
        elif op == "*":
            print(multiply(a,b))
        elif op == "/":
            print(divide(a,b))
        else:
            print("Неизвестная операция.")
