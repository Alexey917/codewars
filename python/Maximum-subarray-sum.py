def max_sequence(arr):
    res = []
    for i in range(len(arr)):
        s = 0
        count = 0
        temp = []
        for j in range(i, len(arr)):
            if j < 0:
                count += 1

            s += arr[j]

            if count == len(arr) - 1:
                s = 0
                temp.append(s)
            else:
                temp.append(s)
        res.append(max(temp))

    print(res)
    max_sum = max(res)

    return max_sum


print(max_sequence([-20, 10, -3, 4, -10, 20, 10, -5, 4]))
