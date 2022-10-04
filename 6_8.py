diction = {
    'Belarus': ['Minsk', 'Gomel', 'Grodno', 'Brest', 'Mogilev', 'Vitebsk'],
    'Italy': ['Milan', 'Rome', 'Venesia'],
    'USA': ['New-York', 'Huston', 'Vermont']

}

for i in range(int(input())):
    country = input().split()
    cities = input().split()
    for city in cities:
        diction[city] = country

for i in range(int(input())):
    print(diction[input()])


