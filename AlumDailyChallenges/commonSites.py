# Input : nate = ["Coding Temple", "GeeksforGeeks", "Udemy", "Coursera"]
#         sam = ["RealPython", "Coding Temple", "Codecademy"]
# Output : ["Coding Temple"]
# -------------------------------
# Input : nate = ["Coding Temple", "GeeksforGeeks"]
#         sam = ["GeeksforGeeks", "Coding Temple", "Codecademy"]
# Output : ["Coding Temple", "GeeksforGeeks"]

# Explanation: There are 2 matches -- "Coding Temple" and "GeeksforGeeks". Coding Temple exists at index 0 of nate's list and idx 1 of sam's list -- the sum is 1. "GeeksforGeeks" exists at idx 1 of nate's list and idx 0 of sam's... so we have a tie and output each!
# -------------------------------
# Input : nate = ["Coding Temple", "GeeksforGeeks"]
#         sam = ["GeeksforGeeks", "Codecademy", "Coding Temple"]
# Output : ["GeeksforGeeks"]

# Explanation: There are 2 matches -- "Coding Temple" and "GeeksforGeeks". "GeeksforGeeks" has a smaller index sum (1) than "Coding Temple" (2), so we return ["GeeksforGeeks"]



def common_places(site_list1, site_list2):
    best_place = ""
    best_index_sum = max(len(site_list1), len(site_list2))
    wompwomp = True 

    places = {v: i for i, v in enumerate(site_list1)}

    for i, place in enumerate(site_list2):
        if place in places:
            # there is a match 
            wompwomp = False 
            index_sum = places[place] + i 
            if index_sum <= best_index_sum:
                best_index_sum = index_sum 
                if best_place == "":
                    best_place += place 
                else:
                    best_place += f", {place}"

    if wompwomp:
        return("You have nothing in common... are you sure you're friends?")

    return best_place
    


nate = ["Coding Temple", "GeeksforGeeks", "Udemy", "Coursera"]
sam = ["RealPython", "Coding Temple", "Codecademy"]
print(common_places(nate, sam))
print("Coding Temple")
print("-------")

nate = ["Coding Temple", "GeeksforGeeks"]
sam = ["GeeksforGeeks", "Coding Temple", "Codecademy"]
print(common_places(nate, sam))
print(["Coding Temple", "GeeksforGeeks"])
print("-------")

nate = ["Coding Temple", "GeeksforGeeks"]
sam = ["GeeksforGeeks", "Codecademy", "Coding Temple"]
print(common_places(nate, sam))
print(["GeeksforGeeks"])
print("-------")

nate = ["udemy", "Coursera"]
sam = ["GeeksforGeeks", "Codecademy", "Coding Temple"]
print(common_places(nate, sam))
print("-------")
