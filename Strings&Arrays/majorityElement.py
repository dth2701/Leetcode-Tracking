class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        # # Count the majority element
        # num_count = defaultdict(int) # {number: count}
        # for num in nums:
        #     num_count[num] += 1
        # # Find key with maximum value     
        # return max(num_count,key=num_count.get)


# Learning Boyer-Moore Voting Algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate