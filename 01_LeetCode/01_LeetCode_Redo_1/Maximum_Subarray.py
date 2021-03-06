"""
Given an integer array nums, find the contigous subarray containing at least one number which has the largest sum
and return its sum. 

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Will use the divide and conquer solution. Using recursion can lead to a stack overflow, it is better to solve it using 
passing window method. 
"""

class Solution:
	def maxSubArray(self, nums):
	# def maxSubArray(self, nums):
		if not nums:
			return -2147483648

		# 
		for i in range(1, len(nums)):
			if nums[i-1] > 0:
				nums[i] += nums[i-1] 
		return max(nums)

x = Solution()

a = [-2,1,-3,4,-1,2,1,-5,4]
print(x.maxSubArray(a))

b = [3, -1, 4]
print(x.maxSubArray(b))

c = [-1, 4]
print(x.maxSubArray(c))

d = [1, 2]
print(x.maxSubArray(d))
