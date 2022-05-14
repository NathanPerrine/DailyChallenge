def searchInsert(nums: list[int], target: int) -> int:
    lowest = 0
    highest = len(nums) -1
    
    if target > nums[-1]:
        return highest +1
    if target < nums[0]:
        return 0
    if target in set(nums):
        return nums.index(target)
        

    while (highest > lowest):
        mid = (lowest + highest) // 2
        if target > nums[mid]:
            lowest = mid + 1
        else:
            highest = mid
        
    return lowest



l1 = [1,2,3,4,5,6,7,8,9,10]
t = 1
print(searchInsert(l1, t))

def searchInsert(self, nums: list[int], target: int) -> int:
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)//2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l