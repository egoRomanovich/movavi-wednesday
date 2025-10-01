def save_result(old_func):
    def new_func(*args, **kwargs):
        result = old_func(*args, **kwargs)
        with open('results.txt', 'a') as f:
            print(f'{result}', file=f)
            # f.write(f'{result}\n')
    return new_func

@save_result
def calculate(a, b, operation='+'):
    """
        Получает на вход два числа и операцию.
        Возвращает результат указанной операции с передаными числами.
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "ОШИБКА: Деление на ноль."
        return a / b
    elif operation == '**':
        return a ** b
    else:
        print('Указанная операция не распознана.')
        return None

calculate(1, 2)
calculate(2, 2, "-")
calculate(3, 2, "**")
