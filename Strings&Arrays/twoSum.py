class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            # Found, return
            if diff in dict:
                return [i, dict[diff]]
            # Not Found, store current num and its index
            dict[num] = i