# returns the total number of treasures buried on the island.
def total_treasures(treasure_map):
    total = 0
    for treasure in treasure_map:
        total += treasure_map[treasure]
    return total

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 

# Problem 2: Pirate Message Check
# returns True if the message contains EVERY letter of the English alphabet at least once, and False otherwise.
def can_trust_message(message):
    # Remove all whitespace and convert to lowercase
    message = message.lower().replace(" ", "")
    
    # Create a set of all letters in the alphabet
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in message:
            return False
    # using len() > 26
    return True

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.
# Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests):
    counter = {}
    result = []
    for chest in chests:
        counter[chest] = 1 + counter.get(chest, 0)
        if counter[chest] == 2:
            result.append(chest)
    return result 

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))

# Problem 4: Booby Trap
#  returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

def is_balanced(code):
    counter = {}

    for letter in code:
        counter[letter] = 1 + counter.get(letter, 0)

    frequencies = list(counter.values())
    print(frequencies)
    count = 0

    first_frequency = frequencies[0]
    for freq in frequencies:
        if freq != first_frequency:
            count += 1
    if count < 1:
        return False
    
    # Return True if there's at most 1 different frequency
    return True

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

# Hello TwoSum
def find_treasure_indices(gold_amounts, target):
    seen = {} #  [num: index] 
    for i, num in enumerate(gold_amounts):
        diff = target - num
        if diff in seen:
            return [i, seen[diff]]
        # store the current number and its index to mark it seen
        seen[num] = i 
    return []
        



gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3)) 
