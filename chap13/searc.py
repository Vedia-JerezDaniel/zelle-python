import numpy as np
nums = np.arange(1, 200000, 1, dtype=int)


def search(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high: # There is still a range to search
        mid = (low + high)//2 # position of middle item
        item = nums[mid]
        if x == item : # Found it! Return the index
            return mid
        elif x < item: # x is in lower half of range
            high = mid - 1 # move top marker down
        else: # x is in upper half
            low = mid + 1 # move bottom marker up
    return -1

search(454, nums)


low = 0
high = len(nums) - 1

def recBinSearch(x, nums, low, high):
    mid = (low + high) // 2
    item = nums[mid]
    if item == x: # Found it! Return the index
        return mid
    elif x < item: # Look in lower half
        return recBinSearch(x, nums, low, mid-1)
    else: # Look in upper half
        return recBinSearch(x, nums, mid+1, high)


recBinSearch(45, nums, low, high)


