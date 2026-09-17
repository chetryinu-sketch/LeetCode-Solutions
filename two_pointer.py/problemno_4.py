"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge_list=sorted(nums1+nums2)
        n=len(merge_list)

        if n%2!=0:
            median=n//2
            return merge_list[median]
        else:
            middle1=n//2-1
            middle2=n//2
            median=(merge_list[middle1]+merge_list[middle2])/2
        return median

obj=Solution()
print(obj.findMedianSortedArrays([1,2],[3,4]))
            

