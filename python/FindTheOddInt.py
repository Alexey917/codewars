def find_it(seq):
    uniq = set(seq)
    result = ''

    for i in uniq:
        print(f'{i} -> {seq.count(i)}')
        if seq.count(i) % 2 != 0:
            result = i
    return result


print(find_it([0, 1, 0, 1, 0, 5, 5, 5, 5, 5]))
