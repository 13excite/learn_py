def strings_checker(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    elif id(str1) == id(str2):
        return 1
    elif (id(str1) != id(str2)) and (len(str1) > len(str2)) and (str2 != 'learn'):
        return 2
    elif (id(str1) != id(str2)) and (str2 == 'learn'):
        return 3
    else:
        return 'Not match'


def main():
    print(strings_checker('abc', 2))
    print(strings_checker('abc', 'abc'))
    print(strings_checker('abcdef', 'abc'))
    print(strings_checker('abcdef', 'learn'))
    print(strings_checker('abc', 'abcdeffffffff'))


if __name__ == '__main__':
    main()
