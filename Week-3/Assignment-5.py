'''
 For example:
 twoSum([2, 7, 11, 15], 9);
 Should returns:
 [0, 1]
 Because:
 nums[0] + nums[1] is 9
'''


# Time Complexity O(n)
def twoSum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return([hash_table[target - num], i])
            break    
        hash_table[num] = i
    return([])
    

print(twoSum([2, 7, 11, 15], 9))