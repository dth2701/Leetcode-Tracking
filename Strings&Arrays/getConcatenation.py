class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        #  nums = [1,3,2,1]
        #  i = 1 , n = 4
        # ans[i + n] == nums[i] => ans[1 + 4] = ans[1]
        # Method 1
        # for i in range(len(nums)):
        #     ans.append(nums[i]) 
        # for i in range(len(nums)):
        #     ans.append(nums[i]) 
        # return ans

        # Method 2
        # n = len(nums)
        # ans = [0] * (2 * n)
        # for i in range(n):
        #     ans[i] =  nums[i]
        #     ans[i+n] = ans[i]
        # return ans

        # Method 3
        return nums * 2