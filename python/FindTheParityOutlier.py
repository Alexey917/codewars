def find_outlier(integers):
    odd = []
    not_odd = []
    for i in integers:
        if i % 2 != 0:
            not_odd.append(i)
        else:
            odd.append(i)
    if len(odd) > len(not_odd):
        return not_odd[0]
    else:
        return odd[0]


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
