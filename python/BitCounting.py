def count_bits(n):
    remainder = []
    if n > 0:
        while n >= 2:
            remainder.append(n % 2)
            n = n // 2
        else:
            remainder.append(n)
        return remainder.count(1)


print(count_bits(123))
