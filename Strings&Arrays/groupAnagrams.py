from collections import defaultdict

def groupAnagrams_defaultdict(strs):
    map = defaultdict(list)  # Creates empty list automatically for new keys
    for word in strs:
        sorted_word = ''.join(sorted(word))
        map[sorted_word].append(word)  # Can append directly!
    return list(map.values())

# Using regular dict:
def groupAnagrams_dict(strs):
    map = {}  # Regular dictionary
    for word in strs:
        sorted_word = ''.join(sorted(word))
        # Need to check if key exists first
        if sorted_word not in map:
            map[sorted_word] = [word]  # Have to create the list manually
        map[sorted_word].append(word)
    return list(map.values())