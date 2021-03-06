"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional 
elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Simply way of solving this. (Using the sort function of Python)
        nums1[:] = sorted(nums1[m:] + nums2)
        # Time: O(n+m * log(n+m)) Space: O(1)
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]
        return nums1.sort()

    # This is the three pointer method, Time: O(n+m) and Space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # We can have three pointers. 
        # The first pointer will start pointing at len(nums) - 1
        # Second pointer will start pointing at m = 3
        p1 = m-1
        p2 = n-1
        p  = len(nums1) - 1
        
        # pointers runs to beginning of the array.
        while p1 >= 0 and p2 >= 0:
            
            # Will stop only at
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
