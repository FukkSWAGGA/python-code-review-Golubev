def add(a, b):
    """Возвращает сумму a и b."""
    return a + b


def subtract(a, b):
    """Возвращает разность a и b."""
    return a - b


def multiply(a, b):
    """Возвращает произведение a и b."""
    return a * b


def divide(a, b):
    """Возвращает результат деления a на b.
    Если делитель равен нулю — возвращает сообщение об ошибке.
    """
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def main():
    """Простой консольный интерфейс калькулятора."""
    print("Простой калькулятор на Python")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'")

    while True:
        user_input = input("\nВведите выражение (например, 2 + 3): ")

        if user_input.lower() == "exit":
            print("Выход из программы.")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: используйте формат 'число операция число'")
                continue

            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("Неизвестная операция.")
                continue

            print("Результат:", result)
        except ValueError:
            print("Ошибка: введите корректные числа.")


if __name__ == "__main__":
    main()
