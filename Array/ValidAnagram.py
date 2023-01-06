# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Questions:
    #?Clarify, the inputs will always be two strings, and we are returning a boolean value based on if they are anagrams
    #?Clarify an anagram is two strings that have the same exact characters and length but not necesarily in the same order

#Edge Cases:
    #Strings of different lengths

#Considerations:
    #Sort the strings immediately and then return their comparison value
    #Track character counts in two separate hashmaps, then iterate through the maps and compare character counts

def validAnagram(s,t):
    if len(s) != len(t):
        return False

    mapS, mapT = {}, {}

    for i in range(len(s)):
        mapS[s[i]] = 1 + mapS.get(s[i], 1)
        mapT[t[i]] = 1 + mapT.get(t[i], 1)

    for char in mapS:
        if mapS[char] != mapT.get(char, 0):
            return False

    return True

s = "anagram"
t = "nagaram"
print(validAnagram(s, t)) #True

s1 = "rat"
t1 = "cat"
print(validAnagram(s1, t1)) #False

s2 = "pero"
t2 = "perro"
print(validAnagram(s2, t2)) #False