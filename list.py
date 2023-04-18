# https://wikidocs.net/1742
# 4. Median of Two Sorted Arrays
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
# https://www.daleseo.com/python-typing/
from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums2 + nums1
        nums.sort()
        if (len(nums) % 2) == 0:
            n = int(len(nums)/2)
            return float((nums[n]+nums[n-1]) / 2)
        else:
            n = int(len(nums)/2)
            return float(nums[n])













