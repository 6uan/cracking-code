
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums):

    # sorted array will be easier to handle
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        # ensures that we don't check if there's duplicates in our "base" index
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # we set our left and right pointers
        #   i   l            r
        # [-4, -1, -1, 0, 1, 2]
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # skips duplicates on our left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # skips duplicates on our right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else: 
                right -= 1 
                
    return result       
        

list = [-1,0,1,2,-1,-4]
print(threeSum(list))