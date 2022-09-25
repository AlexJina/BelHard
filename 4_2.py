s_dict = {}
for i in input():
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1
print(s_dict)

s_dict2 = {}
for i in input():
    s_dict2[i] = s_dict2.get(i, 0) + 1
print(s_dict2)
