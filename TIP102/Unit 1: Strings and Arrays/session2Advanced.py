#  return the first index of target in items, and -1 if target is not in the lst
def linear_search(lst, target):
	# print(list(range(0, len(lst)))) 
	# [0, 1, 2, 3, 4]
	for i in range(0, len(lst)):
		if lst[i].lower() == target.lower():
			print(i)
	print(-1)

def final_value_after_operations(operations):
	if ()

def main():
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    linear_search(items, target)
    linear_search(items, "a")
	

if __name__ == "__main__":
	main()