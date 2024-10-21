def rot13(message):
    result = []
    list(message.encode())
    print(message)
    for let in message:
        let = ord(let) + 13
        result.append(chr(let))
    return ''.join(result)


print(rot13('Hello'))