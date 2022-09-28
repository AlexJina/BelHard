n = int(input())
m = int(input())
k = int(input())
i = 0
while i < n:
    if i > k:
        print(i % m)
    i += 1
print('конец')
