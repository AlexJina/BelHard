
def func(x):
    result = bin(x)
    result_2 = x
    print(result)
    return result_2


print(func(x=int(input())))

def decimal_to_binary(number: int) -> str:
    binary = ''
    while number > 1:
        binary += str(number % 2)
        number //= 2
    binary += str(number)
    return binary[::-1]



def binary_to_decimal(binary: str) -> int:
    number = 0
    for i in binary:
        number *= 2
        number += int(i)
    return number


print(binary_to_decimal('1110'))
