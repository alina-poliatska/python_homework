import string as s

row = input("Введіть рядок: ")
separator = input('Введіть розділювач слів: ')


def sort(words, separator):
    words = row.split(separator)
    res = ''
    result = str()
    for element in sorted(words, key=lambda lenw: len(lenw)):
        res = res + separator + element
        list = res.split(separator)
        result = separator.join(list[::-1])
    return result


print(sort(row, separator))
