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
        dic1[ord(letter)-ord("a")] += 1
    
    for letter in str2:
        dic2[ord(letter) - ord("a")] += 1

    print(dic1, dic2)
    ans = 0
    for i in range(26):
        ans += (abs(dic1[i] - dic2[i]) * (ord("a") + i))
    print(ans)


deletionDistance(str1, str2)