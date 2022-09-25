s_dict = {}
for i in input():
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1
print(s_dict)

s_n = {}
for i in input():
    s_n[i] = s_n.get(i, 0) + 1
