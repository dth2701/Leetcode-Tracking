# Returns the sentence with the order of the words reversed. 
# The sentence will contain only alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function should return the original string.
def reverse_sentence(sentence):

    words_list = sentence.split()
    #  Base Case: Handle one word
    if len(words_list) == 1: return sentence

    reversed_words = []

    # Only alphabetic characters and spaces
    for char in sentence:
        if not(char.isalpha() or char.isspace()):
            return -1
    # [6, 5, 4, 3, 2, 1, 0]
    for i in range(len(words_list) -1 , -1, -1):
        reversed_words.append(words_list[i])
    # reversed_words = words_list[::-1]
    
    return " ".join(reversed_words)
    
# Not min, not max
# Return random number. Else, -1
def goldilocks_approved(nums):
    # Check if list has fewer than 3 numbers
    if (len(nums) < 3): return -1
    
    # Check if only positive int
    for num in nums:
        if num <= 0: return -1

    # Find min, max
    min_val = min(nums)
    max_val = max(nums)

    # look for a number not min and not max
    for num in nums:
        if num != min_val and num != max_val:
            return num
    return -1


# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))
# print(reverse_sentence("Meow"))

# nums = [2, 2, 4, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))


# continuously removes the minimum element until the list is empty. 
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
def delete_minimum_elements(hunny_jar_sizes):
    # base case: only number, 1 number
    if not hunny_jar_sizes: return []
    if len(hunny_jar_sizes) == 1 : return hunny_jar_sizes
    print(sorted(hunny_jar_sizes))

# hunny_jar_sizes = [5, 3, 2, 4, 1]
# delete_minimum_elements(hunny_jar_sizes) #Expected: [1, 2, 3, 4, 5]


# hunny_jar_sizes = [5, 2, 1, 8, 2]
# delete_minimum_elements(hunny_jar_sizes) #Expected: [1, 2, 2, 5, 8]

# Problem 4: Sum of Digits

# accepts an integer num and returns the sum of num's digits.

def sum_of_digits(num):
    total = 0
    while num > 0:
        last_digit = num % 10
        total += last_digit
        # Using floor division to remove last digit
        num = num // 10 
    print(total)

# num = 423
# sum_of_digits(num) #9 # Explanation: 4 + 2 + 3 = 9

# num = 4
# sum_of_digits(num)  #4

# returns True if s is an acronym of words and returns False otherwise.
def is_acronym(words, s):
    if not words or not s: return False
    for i in range(len(words)):
        if s[0].lower() != words[i][0].lower():
            return False
        return True

# words = ["christopher", "robin", "milne"]
# s = "crm"
# print(is_acronym(words, s))

# Problem 7: Good Things Come in Threes
# Return the minimum number of operations to make all elements of nums divisible by 3.
def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if (num + 1) % 3 == 0 or (num - 1) % 3 == 0:
            count += 1
    print(count) 
# nums = [1, 2, 3, 4]
# make_divisible_by_3(nums)

# nums = [3, 6, 9]
# make_divisible_by_3(nums)

def exclusive_elemts(lst1, lst2):
    count_dict = {} # key: item, value: count
    for item in lst1:
        count_dict[item] = count_dict.get(item, 0) + 1
    for item in lst2:
        count_dict[item] = count_dict.get(item, 0) - 1
    
    result = []
    for item, count in count_dict.items():
        # item only appears in one list but not the other.
        if count != 0: 
            result.append(item)
    print(result)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["pooh", "roo", "piglet"]
# exclusive_elemts(lst1, lst2)

# Problem 9: Merge Strings Alternately
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer, append the additional letters onto the end of the merged string.
def merge_alternately(word1, word2):
    if not word1: return word2
    if not word2: return word1
    i = 0
    result = ""
    while i < len(word1) and i < len(word2):
        result += word1[i] + word2[i]
        i += 1
    if len(word1) > len(word2):
        result += word1[i:]
    else:
        result += word2[i:]
    print(result)

# word1 = "wol"
# word2 = "oze"
# merge_alternately(word1, word2)

# word1 = "hfa"
# word2 = "eflump"
# merge_alternately(word1, word2)

# word1 = "eyre"
# word2 = "eo"
# merge_alternately(word1, word2)

# Problem 10: Eeyore's House
def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(0, len(pile1) - 1):
        for j in range(0, len(pile2) - 1):
            if (pile2[j] * k) % pile1[i] == 0:
                count += 1
    print(count)

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# good_pairs(pile1, pile2, k)