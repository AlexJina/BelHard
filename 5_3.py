n = int(input())
numbers = []
for i in range(2, n + 1, 10):
    lst = []
    for j in range(i, i + 9, 2):
        if j > n:
            break
        lst.append(j)
    numbers.append(lst.copy())
print(numbers)
