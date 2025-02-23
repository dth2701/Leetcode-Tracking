# Problem 1: Hunny Hunt
#  return the first index of target in items, 
# and -1 if target is not in the lst
def linear_search(lst, target):
	# print(list(range(0, len(lst)))) 
	# [0, 1, 2, 3, 4]
	for i in range(0, len(lst)):
		if lst[i].lower() == target.lower():
			print(i)
	print(-1)

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# linear_search(items, target)
# linear_search(items, "a")
	

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
def final_value_after_operations(operations):
	# U: handle empty, other different words, lower case and whitespace
	# P: iteration and if-else condition
	# I
	if not operations: return 1
	result = 1
	for operation in operations:
		operation = operation.lower().strip()
		if operation != "bouncy" and operation != "flouncy" and operation != "trouncy" and operation != "pouncy" :
			continue
		if operation == "bouncy" or operation == "flouncy":
			result += 1
		elif operation == "trouncy" or operation == "pouncy":
			result -= 1	
	return result

# operations = ["22ouncy    ", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

# operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))


# Problem 3: T-I-Double Guh-Er II
# returns a new string that removes any substrings t, i, gg, and er from word
def tiggerfy(word):
	# U: handle empty, other different words, lower case and whitespace
	# P: 2 pointers
	# While loop for each letter: 
		# Single case: 't' and 'i' => Compare to add in list and skip index if needed
		# Special case: 'gg' and 'er' 
		# => Combine 2 letters nearby 
		# if matching, skip both indexes
		# else, add the first letter 

	# I
	# Handle empty word
	if not word:
		return ""
	letter_list = []
	i = 0

	while i < len(word):
		# Handle whitespace
		if word[i] == " ":
			i += 1
			continue

		curr_char = word[i].lower()
		# Single case: 't' and 'i'
		if curr_char == 't' or curr_char == 'i':
			i += 1
			continue

		# Special case: 'gg' and 'er'	
		if i + 1 < len(word):	
			next_char = word[i+1].lower()
			# if matching, skip both indexes 
			if curr_char + next_char == "gg" or curr_char + next_char == "er":
				i += 2 
				continue

		letter_list.append(word[i])
		i += 1

	print(''.join(letter_list))
	
# word = "   Trigger  "
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)
	
# Problem 4: Non-decreasing Array
# checks if nums could become non-decreasing by modifying at most one element.
# define an array is non-decreasing 
# if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
# U: Only modifying one time = swap max and min number
# [4, 2, 3, 1]
#  Count the descreasing time 
# Return False if >1
	if not nums:
		return False
	count = 0
	for i in range(0,len(nums) - 1):
		if nums[i] > nums[i+1]:
			count += 1
		if count > 1: 
			return False
	return True


	# i = 0
	# min_num = float('inf')
	# max_num = float('-inf')
	# min_index = -1
	# max_index = -1
	# while i+1 < len(nums):
	# 	curr_num = nums[i]
	# 	next_num = nums[i+1]
	# 	if curr_num > next_num:
	# 		min_num = next_num #2
	# 		max_num = curr_num #4
	# 		min_index = i + 1
	# 		max_index = i
	# 	else:
	# 		continue
	# 	i += 1
	# # Swap min and max at the end
	# temp = nums[min_index] 
	# nums[min_index] = nums[max_index]
	# nums[max_index] = temp

	# return nums
	
# nums = [4, 2, 3] 
# print(non_decreasing(nums)) #Expect True

# nums = [4, 2, 1]
# print(non_decreasing(nums)) #Expect False
	
# Problem 5: Missing Clues
# Return the shortest sorted list of ranges that exactly covers all the missing numbers. 

def find_missing_clues(clues, lower, upper):
	sorted_clues = sorted(clues)
	result = []
	# Compare the first , the middle and the last clue
	# Inclusive!!!
	if clues[0] > lower:
		result.append([lower, clues[0] - 1])
	
	for i in range(len(sorted_clues) - 1):
		if sorted_clues[i] < sorted_clues[i+1] - 1:
			result.append([sorted_clues[i] + 1, sorted_clues[i+1] - 1])

	if sorted_clues[-1] < upper:
		result.append([sorted_clues[-1] + 1, upper])

	return result

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print(find_missing_clues(clues, lower, upper)) #Expected: [[2, 2], [4, 49], [51, 74], [76, 99]]

# clues = [-1]
# lower = -1
# upper = -1
# print(find_missing_clues(clues, lower, upper))