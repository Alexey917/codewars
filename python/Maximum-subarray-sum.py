def max_sequence(arr):
    sums = []
    aaa = []
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        s = 0
        a = []
        arr_flags = []
        for j in range(i, len(arr)):
            flag = True
            if arr[j] < 0:
                flag = False
            arr_flags.append(flag)
            s += arr[j]
            a.append(arr[j])
        if True in arr_flags:
            pass
        else:
            s = 0
        sums.append(s)
        aaa.append(a)
    print(aaa)
    return max(sums)


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
