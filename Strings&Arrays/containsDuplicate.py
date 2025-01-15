class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            # Check if current num in hashset
            if num in hashset:
                return True
            # Otherwise, add current num to hashset
            hashset.add(num)
        return False