s_dict = {}
for i in input():
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1
print(s_dict)
