from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Base case
        if (len(nums) == 0): return 0
        # Tranverse the List
        # in-place = same number is nearby 
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # place curr at position k and inscrease k
                nums[k] = nums[i]
                k += 1
        return k

def main():
    solution = Solution()
    nums1 = []
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums1))
    print(solution.removeDuplicates(nums2))

if __name__ == "__main__":
    main()
