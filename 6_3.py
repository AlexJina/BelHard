spisok = [1, 2, 3, 4, 5, 6, 7]
n = int(input())
print(spisok[-n:] + spisok[:-n])


def shik(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


spisok = [1, 2, 3, 4, 5, 6, 7]
shik(spisok, 3)
print(spisok)
