def search(nums: list[int], target: int) -> int:
    if target in set(nums):
        return nums.index(target)
    return -1



print(search([1,2,3,4,5], 2))