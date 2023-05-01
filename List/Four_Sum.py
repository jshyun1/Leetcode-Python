from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        for j in range(len(nums) - 3):
            for i in range(j+1, len(nums) - 2):
                left = i + 1
                right = len(nums) - 1
                # 투 포인터 전략을 사용하자
                while left < right:
                    summation = nums[j] + nums[i] + nums[left] + nums[right]
                    if summation < target:
                        left += 1
                    elif summation > target:
                        right -= 1
                    else:
                        result.add((nums[j], nums[i], nums[left], nums[right]))
                        # 리스트는 set 에서 해쉬 처리가 되지 않기 때문에 튜플로 바꾸어서 해결하자.

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return list(map(list, result))