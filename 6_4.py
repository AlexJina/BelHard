so_list = ['dog', 656, 'cat', 'seryu', 6780, 5, 6, 'kkikl']
a = [x for x in so_list if type(x) == str]
print(a)

so_lis = ['dog', 656, 'cat', 'seryu', 6780, 5, 6, 'kkikl']
so_lis = list(filter(lambda x: type(x) == str, so_lis))
print(so_lis)
