def twoSum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def main():
    nums = [2, 7, 11, 15]
    target = int(input("Enter a number you want the sum to: "))
    print(twoSum(nums, target))


if __name__ == "__main__":
    main()
