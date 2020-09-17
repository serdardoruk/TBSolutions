str1 = "123"
str2 = "abc"

str1 = "4567"
str2 = "d"
def interleave(str1, str2):
    i = 0
    j = 0

    newStr = ""
    isOne = True
    while i < len(str1) and j < len(str2):
        if isOne:
            newStr += str1[i]
            i += 1
            isOne = False
        else:
            newStr += str2[j]
            j += 1
            isOne = True

    
    if i < len(str1):
        newStr += str1[i : ]
    
    if j < len(str2):
        newStr += str2[j : ]

    return newStr

print(interleave(str1, str2))
