# returns the length of the longest balanced subsequence.
# A balanced collection = the difference between the max and min value of the art pieces = 1.
# No changing the order of the remaining elements.

def find_balanced_subsequence(art_pieces):
    # Base case: If all values are the same, there's no balanced subsequence

    if len(set(art_pieces)) == 1:
        return 0
    # {1, 2, 3, 5, 7}
    count = {}
    for piece in art_pieces:
        count[piece] = 1 + count.get(piece, 0)
    
    # Check each potential pair
    max_length = 0
    for value in count:
        if value + 1 in count:
            max_length = max(max_length, count[value] + count[value + 1])
    return max_length


# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

# Problem 2: Verifying Authenticity
# returns True if the given array is an authentic array, and otherwise returns False.
# base[n] = [1, 2, ..., n - 1, n, n]
# "authentic" if the list is a permutation of an array base[n].
# Note: A permutation of integers represents an arrangement of these numbers. 

def is_authentic_collection(art_pieces):

    n = len(art_pieces)
    if n == 0: return False

    # Find the highest number in the collection
    max_num = max(art_pieces)  
    if max_num + 1 != n: return False

    counter = {}

    for num in art_pieces:
        counter[num] = 1 + counter.get(num , 0)

        
    # Check values 1 to n-1 occur exactly once
    for i in range(1, max_num):
        if counter.get(i, 0) != 1:
            return False
        
    # Check that value n occurs exactly twice
    if counter.get(max_num, 0) != 2:
        return False
    
    return True

    # n = len(art_pieces)
    # sorted_art_piece = sorted(art_pieces)
    # authentic_arr = list(range(1, n))
    # authentic_arr.append(n-1)
    # return sorted_art_piece == authentic_arr



collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1)) #False
print(is_authentic_collection(collection2)) #True
print(is_authentic_collection(collection3)) #True

# Problem 3: Gallery Wall

# 1.The 2D array should contain only the elements of the array collection.
# 2. Each row in the 2D array should contain distinct strings. using set()
# 3. The number of rows in the 2D array should be minimal. using % 2 == 0
# Return the resulting array. If there are multiple answers, return any of them. 
# Note that the 2D array can have a different number of elements on each row. 

# U
# 
# def organize_exhibition(collection):
#     # new_collection = set(collection)
#     counter = {}
#     for str in collection:
#         counter[str] = 1 + counter.get(str, 0)
    
#     result = []
#     for str, count in counter.items(): 
#         if str


#         # if str not in result:
#         #     result[str] = []




#     return counter

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
#               "Kahlo", "O'Keefe"]

# print(organize_exhibition(collection1))
