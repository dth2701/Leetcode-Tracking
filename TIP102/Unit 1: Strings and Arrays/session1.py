def welcome():
    return("Welcome to The Hundred Acre Wood!")    

def greeting(name):
    return(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

def print_catchphrase(character):
    match (character):
        case "Pooh":
            return("Oh bother!")
        case "Tigger":
            return("TTFN: Ta-ta for now!")
        case "Eeyore":
            return("Thanks for noticing me.")
        case "Christopher Robin":
            return("Silly old bear.")
        case _:
            return(f"Sorry! I don't know {character}'s catchphrase!")

# returns the element at index x in items. 
# If x is not a valid index of items, return None.
def get_item(items, x):
    return items[x] if x in range(0, len(items)) else None

# returns the sum of all elements in the list
def sum_honey(hunny_jars):
    total = 0
    if len(hunny_jars) == 0: return "hello 0"
    for jar in hunny_jars:
        total += jar
    return total

# return the number of race times less than threshold.
def count_less_than(race_times, threshold):
    # count = 0
    # for race in race_times:
    #     if race < threshold:
    #         count += 1
    # return count
    return len([ race for race in race_times if race < threshold])

# Input: a list of strings named tasks. 
# The function should then number and print each task on a new line

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
# ...
def print_todo_list(task):
    print("Pooh's To Dos:")
    order = 1
    for i in range(0,len(task)):
        print(f"{order}. {task[i]}")
        order += 1

# returns a list of all divisors of quantity.
def split_haycorns(quantity):
    result = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)
    return result

#  returns a new string without the letters t, i, g, e, and r from it.
def tiggerfy(s):
    newStr = ""
    for char in s:
        if char.upper() not in "TIGER":
            newStr += char
    return newStr    

#  returns a list of the indices of any elements with value "thistle"
def locate_thistles(items):
    if not items:
        return []
    result = []
    for i in range(0, len(items)):
        if items[i].lower() == "thistle":
            result.append(i)
    return result

def main():
    # print(welcome())

    # name = "Amy"
    # print(greeting(name))
    
    # print(print_catchphrase("cat"))
    # print(print_catchphrase("Eeyore"))

    # items = ["piglet", "pooh", "roo", "rabbit"]
    # print(get_item(items, 3))
    # print(get_item(items, 5))

    # hunny_jars = [2, 3, 4, 5]
    # print(sum_honey(hunny_jars))
    # print(sum_honey([]))

    # race_times = [1, 2, 3, 4, 5, 6]
    # threshold = 4
    # print(count_less_than(race_times, threshold))
    # print(count_less_than([], threshold))

    # task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    # print_todo_list(task)
    
    # print(split_haycorns(6))

    # s = "suspicerous"
    # print(tiggerfy(s))

    # items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    # print(locate_thistles(items))

if __name__ == "__main__":
    main()