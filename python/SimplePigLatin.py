import re


def pig_it(text):
    result = []
    for word in text.split(' '):
        if re.search(r'[!.,?\"\']', word):
            word += word[0]
        else:
            word += word[0] + "ay"
        result.append(word[1:])

    result = ' '.join(result)
    return result


pig_it('Pig latin is cool')
