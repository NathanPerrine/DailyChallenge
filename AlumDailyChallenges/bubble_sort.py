# Basic sorting


def bubble_sort(alist):
    is_sorted = False

    while not is_sorted:
        is_sorted = True 

        for i in range(len(alist) -1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False

    return alist

unsorted = [3, 1, 5, 3, 0 , 7, 10, 40, 1, 50, 100]
# print(unsorted)
# print(bubble_sort(unsorted))
# print(unsorted)



def bubble_2(alist):
    # Flag to check if the list is sorted and break loop
    is_sorted = False 
    
    while not is_sorted:
        # Assume list is sorted
        is_sorted = True 
        # Loop through list (-1 since we're doing i+1 later)
        for i in range(len(alist)-1):
            # Check to see if the current value is greater than the next value
            if alist[i] > alist[i+1]:
                #If true, swap values and reset flag
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False 
    return alist

# print(unsorted)
# print(bubble_2(unsorted))
# print(unsorted)

def bubble_3(alist):
    ''' Minor optimization, since bubble sort puts the highest numbers to the top you don't need to reach the top of the list every time'''
    
    is_sorted = False 
    iterations = 0

    while not is_sorted:
        is_sorted = True 

        for i in range(len(alist)) - iterations -1:
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False 

        iterations += 1
    return alist

print(unsorted)
print(bubble_2(unsorted))
print(unsorted)