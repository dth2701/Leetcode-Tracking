class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap: {sorted_word: List}
        # Compare count for each letter
        if not strs:
            return []
        map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # add the new word to list 
            map[sorted_word].append(word)
        return(list(map.values()))