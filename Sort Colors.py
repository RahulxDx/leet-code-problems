''' class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for passes in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
'''

# Right Answer
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = ([0] * nums.count(0)) + ([1] * nums.count(1)) + ([2] * nums.count(2))
        return nums
