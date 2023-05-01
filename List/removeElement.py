from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)