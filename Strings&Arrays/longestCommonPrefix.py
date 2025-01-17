class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Base case
        if not strs:
            return ""
        result = ""
        # Get the first word to compare with others
        for i in range(len(strs[0])):
            for word in strs:
                # Compare current char with same position on other word
                # Check out of bound of current str to return
                if i == len(word) or word[i] != strs[0][i]:
                    return result
            # Add the letter of the the first word because it is a prefix
            result += strs[0][i]
        return result