# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

from collections import Counter
def isAnagram(s,t):
        # if len(s)==len(t):
        #     if ''.join(sorted(s))==''.join(sorted(t)):
        #         return True
        #     else:
        #         return False
        return Counter(s)==Counter(t)
        # return sorted(s)==sorted(t)
print(isAnagram("anagram","nagaram"))