def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    map1 = {}
    map2 = {}

    for i in range(len(s)):

        if s[i] not in map1:
            map1[s[i]] = t[i]

        elif map1[s[i]] != t[i]:
            return False

        if t[i] not in map2:
            map2[t[i]] = s[i]

        elif map2[t[i]] != s[i]:
            return False

    return True

def main():
    s = input("Enter a word: ")
    t = input("Enter a seccond word: ")

    print(f"The words {s} and {t} are isomorphic? -> ", isIsomorphic(s, t))

if __name__ == "__main__":
    main()