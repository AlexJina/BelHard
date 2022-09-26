number_1 = float(input())
operation = str(input())
number_2 = float(input())
if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/' and number_2 != 0:
    print(number_1 / number_2)
elif operation == '/' and number_2 == 0:
    print('Деление на 0!')
elif operation == 'mod' and number_2 == 0:
    print('Деление на 0!')
elif operation == 'mod' and number_2 != 0:
    print(number_1 % number_2)
elif operation == 'pow':
    print(number_1 ** number_2)
elif operation == 'div' and number_2 != 0:
    print(number_1 // number_2)
elif operation == 'div' and number_2 == 0:
    print('Деление на 0!')
