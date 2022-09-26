# Заполнить список четными числами в квадрате от 1 до N
#n = int(input())
#s_list = []
#for i in range(2, n, 2):
#    if not i % 2:
 #       s_list.append(i ** 2)
#print(s_list)
# В строке, определить количество не пересекающихся пар одинаковых символов
words = input()
c = 0
i = 0
while i < len(words) - 1:
    if words[i] == words[i+1]:
        c += 1
        i += 1
    i += 1
print(c)

# Спрашивать у пользователя даные с клавиатуры, пока он не введет числа
#number = input()
#while not number.isdigit():
 #   number = input()
