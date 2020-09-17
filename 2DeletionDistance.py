'''
min number of characters that you need to delete in the two strings in order to have the same string. The deletion distance between 'cat' and 'at' is 1,
beacause tou can just delete the first character of cat. The deletetion distance between...
'''

str1 = "at"
str2 = "cat"

str1 = "boat"
str2 = "got"

str1 = "thought"
str2 = "sloughs"

def deletionDistance(str1, str2):
    dic1 = [0 for i in range(26)]
    dic2 = [0 for i in range(26)]

    for letter in str1:
        dic1[ord("a") - ord(letter)] += 1
    
    for letter in str2:
        dic2[ord("a") - ord(letter)] += 1

    print(dic1, dic2)
    ans = 0
    for i in range(26):
        ans += (abs(dic1[i] - dic2[i]))
    print(ans)


deletionDistance(str1, str2)