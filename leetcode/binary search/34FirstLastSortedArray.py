# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]


def searchRange(nums: list[int], target: int) -> list[int]:
    # Double binary search to find upper and lower bounds
    l, h = 0, len(nums) -1
    # lower index
    first = findFirstIndex(nums, l, h, target)
    # upper index
    second = findLastIndex(nums, l, h, target)
    return [first, second]

def findFirstIndex(nums, low, high, target):
    res = -1 
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            # found the target so we're limiting the high end to get the lower bound
            high = mid - 1
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid + 1
    return res
def findLastIndex(nums, low, high, target):
    res = -1
    while low <= high:
        mid = (low + high) // 2 
        if nums[mid] == target:
            res = mid
            # found the target so we're limiting the low end to get the upper bound
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return res


nums = [5,7,7,8,8,10] 
target = 8
print(searchRange(nums, target))