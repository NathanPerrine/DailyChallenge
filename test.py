# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

def commonPlaces(l1, l2):
    possiblePlaces = {}
    for index, r in enumerate(l1):
        for index2, r2 in enumerate(l2):
            if r == r2:
                possiblePlaces[r] = index + index2
    finalPlaces = possiblePlaces.values()
    
    final = [x for x in possiblePlaces.keys() if possiblePlaces[x] == min(finalPlaces)]
    return final

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# print(commonPlaces(list1, list2))

list1 = ["Shogun","Burger King", "Tapioca Express","KFC"]
list2 = ["Burger King", "Shogun", "KFC"]
print(commonPlaces(list1, list2))