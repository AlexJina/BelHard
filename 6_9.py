data = {
    1: {
        'name': 'Alex',
        'email': 'info@info.com'
    },
    2: {
        'name': 'Pavel',
        'email': ''
    },
    3: {
        'name': 'Vasya'

    }
}
for user in data.values():
    if 'email' not in user or not user['email']:
        print(user['name'])

