
def check_number(x):
    try:
        x = float(x)
    except ValueError:
        
        return True        
    else:
        global a
        a = float(x)
        return False

def check_operation(x):
    if x in list_of_math_operations:
        global math_operation
        math_operation = x
        return False
    else:
        return True

list_of_math_operations = ['+', '-', '*', '/', '//', '%', '**', '*%']

math_operation_discription = '''
    Выберите действие:
    Знак "+" - сложение
    Знак "-" - вычитание второго числа из первого
    Знак "*" - умножение двух чисел
    Знак "/" - деление первого числа на второе
    Знак "//" - деление первого числа на второе, без остатка
    Знак "%" - выводит остаток от деления первого числа на второе
    Знак "**" - возводит первое число в степень значения второго числа
    Знак "*%" - выводит процент (второе число) от первого числа    
'''
repeat = 1

while repeat:
    while check_number(input('Введите первое число: ')):
        print('Нужно ввести число, попробуйте еще раз.')
    number1 = a

    while check_operation(input(math_operation_discription)):
        print('Нужно выбрать операцию из списка. Попробуйте еще раз')

    while check_number(input('Введите второе число: ')):
        print('Нужно ввести число, попробуйте еще раз.')
    number2 = a

    if math_operation == '+':
        print(f'{number1} + {number2} = {number1 + number2}')
    elif math_operation == '-':
        print(f'{number1} - {number2} = {number1 - number2}')
    elif math_operation == '*':
        print(f'{number1} * {number2} = {number1 * number2}')
    elif math_operation == '/':
        print(f'{number1} / {number2} = {number1 / number2}')
    elif math_operation == '//':
        print(f'{number1} // {number2} = {number1 // number2}')
    elif math_operation == '%':
        print(f'остаток от деления {number1} на {number2} = {number1 % number2}')
    elif math_operation == '**':
        print(f'{number1} в степени {number2} = {number1 ** number2}')
    elif math_operation == '*%':
        print(f'{number2} процентов от {number1} = {number2 * number1 / 100}')

    repeat = input('Для повторного запуска введите любой символ. Для выхода просто нажмите Enter: ')

print('Пока!')