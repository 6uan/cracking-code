
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.


def findMaxAverage(nums, k):
    #            vvvvvv  
    # get sum of [0...k..n]
    current_max = sum(nums[:k])

    # stores current max to compare with later max
    max_sum = current_max
    #               vvvvv
    # range is [0...k..n] 
    for i in range(k, len(nums)):
        # gets k range of elements (sliding window)
        current_max += nums[i] - nums[i - k]
        # compares current and earlier max sum
        max_sum = max(max_sum, current_max) 
    # convert to float to preserve decimal  
    avg = float(max_sum) / k
    return avg
    


list = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(list, k))