# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:
# Input: nums = [1,2,3]
# Output: 0
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# O(n) Time | O(n) Space 

def num_good_pairs(nums):
    # Crate a dict to store numbers we've seen and their frequency 
    seen = {}
    # Count to count each pair
    count = 0

    for num in nums:
        # If the number is already in the seen dict, we have a duplicate
        # Add the frequency to the total count
        # Add 1 to the frequency value
        if num in seen:
            count += seen[num]
            seen[num] += 1
        else: 
            seen[num] = 1 

    return count 

nums = [1,2,3,1,1,3]
print(num_good_pairs(nums))