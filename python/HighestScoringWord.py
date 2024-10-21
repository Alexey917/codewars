def high(x):
    point_arr = {}
    string = x.lower().split(' ')
    max_value = 0

    for char in string:
        point = 0
        list(char)
        for c in char:
            point += ord(c) - 96
        point_arr[char] = point

    for key, value in point_arr.items():
        if value > max_value:
            max_value = value

    for key, value in point_arr.items():
        if value == max_value:
            return key


print(high('hello world'))
