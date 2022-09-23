name = input()
age = int(input())
city = input()
print(f'Привет, меня зовут {name}, мне {age} лет, я живу в {city}')

name = input()
age = int(input())
city = input()
print('Моё имя {} , мне {} лет ,я живу в {}'.format(name, age, city))

name = input()
age = int(input())
city = input()
print('Моё имя %(name)s , мне %(age)d лет ,я живу в %(city)s' % {"name":name, "age":age, "city":city})
