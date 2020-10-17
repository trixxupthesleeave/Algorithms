"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
Example 3:

Input: s = "a", t = "aa"
Output: "a"
Example 4:

Input: s = "ae", t = "aea"
Output: "a"
"""

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # Each distinct string and store it in dictionary. 
        if not s:
            return t
        c = Counter(s)
        
        # Decrement count of eack key while traversing t. 
        # If a character is not in dicitonary or count is less < 0. Return that value. 
        for i in t:
            if i in c:
                c[i] -= 1
                if c[i] < 0:
                    return i
            else:
                return i
        