A = [1, 0, 1, 1, 1]

# With this function, you insert a list of numbers, and it will return the maximum amount
#   of consecutive '1s' in that list of numbers.
def ConsecutiveOnes(A):
    maxOnes = 0
    tempOnes = 0
    for i in range(len(A)):
        if A[i] == 1:
            tempOnes += 1
        else:
            if tempOnes > maxOnes:
                maxOnes = tempOnes
            tempOnes = 0
    if tempOnes > maxOnes:
        maxOnes = tempOnes
    return maxOnes


print(ConsecutiveOnes(A))

