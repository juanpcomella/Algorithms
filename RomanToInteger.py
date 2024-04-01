def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0

    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            integer -= roman[s[i]]
        else:
            integer += roman[s[i]]

    integer += roman[s[-1]]

    return integer


def main():
    s = input('Enter a number in roman numerals: ')
    print(romanToInt(s))


if __name__ == '__main__':
    main()
