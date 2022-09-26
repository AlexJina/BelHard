k = int(input())
m = int(input())
n = int(input())
for i in range(n):
    if i % k and i < m:
        i += 1
    print(i)
