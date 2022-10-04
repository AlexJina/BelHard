def my_reverse(lst: list) -> list:
    for i in range(len(lst) // 2):
        lst[i], lst[~i] = lst[~i], lst[i]
    return numbers


numbers = [1, 2, 3, 4, 5, 6, 7]
print(my_reverse(numbers))
