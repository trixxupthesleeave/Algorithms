"""
There are several cards arranged in a row, and each card has an associated number of points The points are
given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k
cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will 
maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score 
of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202

Constraints:
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""

class Solution:

    # Mem Constraint / Time Limit Exceeded. (Recursion with memo won't cut it)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        if k == 1:
            return max(cardPoints[-1], cardPoints[0])
        return self.findMax(cardPoints, k, 0, {})
    
    def findMax(self, points, k, tot, mem):
        if k == 0:
            return tot
        temp = str(points)
        if temp in mem:
            return mem[temp]
        mem[temp] = max(self.findMax(points[1:], k-1, tot+points[0], mem), self.findMax(points[:-1], k-1, tot+points[-1], mem))
        return mem[temp]

    # Sliding window 
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        best = total
        for _ in range(k):
            total += cardPoints[left] - cardPoints[right]
            best = max(best, total)
            left += 1
            right += 1
        return best 