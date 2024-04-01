def isPalindrome(x):
    x_str = str(x)
    left = 0
    right = len(x_str) - 1
    if right == 0:
        return True
    while left <= right:
        if x_str[left] != x_str[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    x = input("Enter a word or number to see if its a palindrome: ")
    print(isPalindrome(x))


if __name__ == "__main__":
    main()
