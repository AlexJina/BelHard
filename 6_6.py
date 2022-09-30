s_num_list = [2, 4, 6, 12, 34, 5, 7, 9, 11, 45, 23]

a = [x for x in s_num_list if not x % 2]
b = [x for x in s_num_list if x % 2]
print(a + b)
