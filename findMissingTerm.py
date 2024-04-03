
# With this algorithm, it determines a pattern in a list and tells you which number is missing,
# the thing is that there will always only be one missing item.

A = [2,4,6,10,12,14]
left = A[0]
right = max(A)

def findMissing(A, left, right):
    n = len(A)
    i = 1
    cons = (right-left)//n
    while i < n:
        if A[i + 1] - A[i] == cons:
            i += 1
        else:
            missing = A[i] + cons
            return missing

print(findMissing(A, left, right))

