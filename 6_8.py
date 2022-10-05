diction = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        diction[city] = country

for i in range(int(input())):
    print(diction[input()])
