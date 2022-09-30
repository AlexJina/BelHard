n = int(input())
m = int(input())
k = int(input())
while n:
    if not k % m:
        print(k)
        n -= 1
    k += 1
