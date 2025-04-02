# Time Complexity - O(n) | Space Complexity - O(1)
class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]

        for i in range(0, len(nums)):
            if abs(closest) == abs(nums[i]):
                if nums[i] > closest:
                    closest = nums[i]
            elif abs(closest) > abs(nums[i]):
                closest = nums[i]
        return closest
