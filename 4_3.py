n = int(input('n: '))

users = {
    i: {
        'name': input(f'{i} name: sasha'),
        'email': input(f'{i} email: sasha@mail.ru')
    } for i in range(n)
}
print(users)
