'''
A palindrome is a string which reads thesame forwards as backwards, for example 'abba' or 'racecar' or 'bob'. Write a function which returns the length of
the longest palindromic substring of a given string. For example, the longest palindromix substring of 'bobcat' is 'bob', so you'd return 3. You do not need
to come up with an optimized algorithm for this. A simple search through all substrings is fine.
'''

string = "bobcat"
string2 = "racecargibi"

def longest(string):
    longest = 1
    
    for i in range(1, len(string)):
        odd = string[longest - 1 : i]
        even = string[longest - 1 : i + 1]

        if odd == odd[::-1]:
            longest = max(longest, len(odd))

        if even == even[::-1]:
            longest = max(longest, len(even))

    return longest

print(longest(string))
print(longest(string2))