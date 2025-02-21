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

# continuously removes the minimum element until the list is empty. 
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
def delete_minimum_elements(hunny_jar_sizes):
    # base case: only number, 1 number
    if len(hunny_jar_sizes) == 0 : return 0
    if len(hunny_jar_sizes) == 1 : return hunny_jar_sizes[1]


def main():
    # sentence = "tubby little cubby all stuffed with fluff"
    # print(reverse_sentence(sentence))
    # print(reverse_sentence("Meow"))

    # nums = [2, 2, 4, 4]
    # print(goldilocks_approved(nums))

    # nums = [1, 2]
    # print(goldilocks_approved(nums))

    # nums = [2, 1, 3]
    # print(goldilocks_approved(nums))

if __name__ == "__main__":
    main()