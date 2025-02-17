from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Removing val in nums
        # Return the count of remaining elements in nums
        # Time complexity: O(n2) because for each val we find
        # Space Complexity: O(1)
        while val in nums: 
            nums.remove(val)
        nums.sort() # O(nlogn)

        return len(nums)

def main():
    solution = Solution()
    test_nums = [0,1,2,2,3,0,4,2]
    test_val = 2
    print(test_nums)
    result = solution.removeElement(test_nums, test_val)
    print(result)

if __name__ == "__main__":
    main()
        # IN PLACEEEEEE
        # [0,1,2,2,3,0,4,2]
        # val = 2
        # i = 0: nums[0] = nums[0] = 0, count = 1
        # i = 1: nums[1] = nums[1] = 1, count = 2

        # i = 4: nums[2] = nums[4] => nums[2] = 3, count = 3
        # i = 5:  nums[3] = nums[5] => nums[3] = 0, count = 4
        # i = 6:  nums[4] = nums[6] => nums[4] = 4, count = 5
        # 0,1,3,0,4


        # Better Method 
        # Time complexity: O(n) because for each val we find
        # Space Complexity: O(1)
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         # Found, put it as position k and move k Forward
        #         nums[count] = nums[i]
        #         count+=1 
        # return count
    