line1 = input('Введите строку 1: ')
line2 = input('Введите строку 2: ')


def comparison (line1, line2):
    if type(line1) != str or type(line2) != str:
        print(0)
    elif line1 == line2:
        print(1)
    elif line1 != line2 and len(line1) > len(line2) and line2 != 'learn':
        print(2)
    elif line1 != line2 and line2 == 'learn':
        print(3)

print(comparison(line1, line2))
