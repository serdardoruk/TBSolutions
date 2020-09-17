def match(brackets):
    stack = []
    for p in brackets:
        if p == ")":
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)
        else:
            stack.append(p)

    
    return len(stack) == 0


# brackets = "(()()))"
brackets = "((())"
brackets = "())"

print(match(brackets))

