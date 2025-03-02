# Parameter: a list of dictionaries 
# return the name of the species with the lowest population.
def most_endangered(species_list):
    # print(species_list[0]["population"])
    min_population = float('inf')
    name_population = ""
    for i in range(len(species_list)):
        curr_population = species_list[i]["population"]
        if curr_population < min_population:
            min_population = curr_population
            name_population = species_list[i]["name"]
        
    return name_population

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))


# Count different endangered species in the observed list.
# Problem 2: Identifying Endangered Species
def count_endangered_species(endangered_species, observed_species):
    # A list of unique endangered species
    new_endangered_species = set(endangered_species)
    count = 0
    for i in range(len(observed_species)):
        if observed_species[i] in new_endangered_species:
            count += 1
    return count

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

# Problem 3: Navigating the Research Station
# Starting from 0
# The time taken to move from one observation point to another = |i - j|.
# returns the total time it takes to visit all the required observation points in the given order with one movement.

def navigate_research_station(station_layout, observations):

    # key: char, value: index
    station_positions = {}
    for i, char in enumerate(station_layout):
        station_positions[char] = i

    # Moving index
    total = 0
    current_index = 0
    for observation in observations: 
        # Get the index of observation in station
        observation_index = station_positions[observation]
        total += abs(observation_index - current_index)
        # Update to the current index
        current_index = observation_index
    return total

# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"
# print(navigate_research_station(station_layout1, observations1))  #Expected: 45
 
# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"
# print(navigate_research_station(station_layout2, observations2)) # Expected: 4
# Example 2 explanation: The index moves from 0 to 2 to observe 'c', then to 1 for 'b', then to 0 again for 'a'.
# Total time = 2 + 1 + 1 = 4.


# Problem 4: Prioritizing Endangered Species Observations

# priority_species: unique
# observed_species: need to be sorted
# Mission: sorts the elements of observed_species
# such that the relative ordering of items in observed_species matches that of priority_species
# Species that do not appear in priority_species should be placed at the end of observed_species in ascending order. hint: extend()
def prioritize_observations(observed_species, priority_species):
    
    # append same items slowly in the list
    seen = [] # A dict of non-priority items to keep track
    result = []
    dict = {} # key: item, value: count
    for specie in observed_species:
        if specie in priority_species:
            dict[specie] = 1 + dict.get(specie, 0)
        else:
            seen.append(specie)
    
    # Add priority species in the order they appear in priority_species
    for specie in priority_species:
        if specie in dict: 
            count = dict[specie]   
            while count > 0:
                result.append(specie)
                count -= 1

    result.extend(seen)
    return result

# observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
# priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  
# print(prioritize_observations(observed_species1, priority_species1))

# observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
# priority_species2 = ["cardinal", "sparrow", "bluejay"]
# print(prioritize_observations(observed_species2, priority_species2)) #["cardinal", "sparrow", "bluejay", "crow", "robin"]


# Problem 5: Calculating Conservation Statistics
# 1. Find the species with the minimum population and remove it.
# 2. Find the species with the maximum population and remove it.
# 3. Calculate the average population of the two removed species.
# Return # distinct averages calculated using the above process.

def distinct_averages(species_populations):
    species_populations.sort()
    i = 0
    average_val = 0
    count = 0
    l, r = 0, len(species_populations) - 1
    while l < r:
        min_val = species_populations[l]
        max_val = species_populations[r]
        new_average_val = (min_val + max_val)/2
        l += 1
        r -= 1
        if average_val != new_average_val:
            count += 1
        average_val = new_average_val
    return count

    
# species_populations1 = [4,1,4,0,3,5]

# print(distinct_averages(species_populations1))

# Problem 6: Wildlife Reintroduction

# U:
# raised_species : the list of species available 
# target_species: a specific sequence of species 
# Return the max_num of copies of target_species that can be formed by taking species from raised_species and rearranging them.

def max_species_copies(raised_species, target_species):
    raised_counter, target_counter = {}, {}
    for specie in raised_species:
        raised_counter[specie] = 1 + raised_counter.get(specie, 0)
    for specie in target_species:
        target_counter[specie] = 1 + target_counter.get(specie, 0)

    # Base case: Handle the case that we are missing the available species
    if len(raised_counter) < len(target_counter):
        return 0

    min_copies = float('inf')

    for species, count_needed in target_counter.items():
        
        # No copies founded
        if species not in raised_counter:
            return 0 
        
        # Counting min_copies based on raised_species
        needed_copies = raised_counter[specie] // count_needed
        min_copies = min(min_copies, needed_copies)
    return min_copies

# raised_species2 = "aaaaabbbbcc"
# target_species2 = "abc"
# print(max_species_copies(raised_species2, target_species2)) # Output: 2


# Problem 7: Count Unique Species
# Return the number of UNIQUE species counts after performing the replacement operations on ecosystem_data.

def count_unique_species(ecosystem_data):
    i = 0
    unique_num = set()
    while i < len(ecosystem_data):
        number= ""
        # Found a digit (the started)
        if ecosystem_data[i].isdigit():
            # Extract the full number
            while i < len(ecosystem_data) and ecosystem_data[i].isdigit():
                number += ecosystem_data[i]
                i += 1
            # Add that full number to a set of unique num
            unique_num.add(int(number)) #Handle 01, 00
        # Otherwise, go to next position
        else:
            i += 1

    return len(unique_num)       

# ecosystem_data1 = "f123de34g8hi34"
# print(count_unique_species(ecosystem_data1))

# ecosystem_data3 = "x1y01z001"
# print(count_unique_species(ecosystem_data3))

# Problem 8: Equivalent Species Pairs
# a list [a, b] where a and b represent two species observed together.
#  [a, b] is equivalent to [c, d] <> either (a == c and b == d) or (a == d and b == c)
# Return #equivalent_pairs in the list of observed species pairs.
# Hint: c * (c - 1) // 2 
# for [1,2] : 3 * (3-1) // 2 = 3
def num_equiv_species_pairs(species_pairs):
    # Tranverse to each pair
    counter = {}
    for pair in species_pairs:
        counter[tuple(pair)] = 1 + counter.get(tuple(pair), 0)

    pairs = 0
    for value in counter.values():
        if value > 1:
            pairs += value * (value -1) // 2 #3+0+0
    return pairs

species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(num_equiv_species_pairs(species_pairs2))
