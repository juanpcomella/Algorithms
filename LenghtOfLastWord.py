def lenghOfLastWord(s):
    words = s.strip().split(' ')
    return len(words[-1])

def main():
    s = input('Enter a string: ')
    print(lenghOfLastWord(s))

if __name__ == '__main__':
    main()