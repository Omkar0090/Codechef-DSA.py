Largest Odd Substring

# You are given a string numsnums consisting of digits representing a large integer. Your task is to find the largest-valued odd integer (as a substring of numsnums) that can be obtained.
# A substring is a contiguous sequence of characters within the string.

CODE = 

def findLargestOddSubstring(nums):
    for i in range(len(nums)-1, -1, -1):
        if int(nums[i]) % 2 != 0:
            return nums[:i+1]
    return "-1"
