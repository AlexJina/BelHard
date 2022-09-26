n = int(input())
m = int(input())
k = int(input())
i = 0
while n > k:
    if n % m == 0:
        print(i)
    i += 1
