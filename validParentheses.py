def isValid(s):

    stack = []
    brackets = {"(" : ")", "[" : "]", "{" : "}"}

    for bracket in s:
        if bracket in brackets:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != brackets[stack.pop()]:
            return False

    if len(stack) == 0:
        return True
    else:
        return False