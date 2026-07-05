MIN To MAX

CODE = 

class Solution:
    def count_non_minimum(self, nums):
        if not nums:
            return 0
        
        # 1. Find the minimum value M in the initial array.
        minimum_value = min(nums)
        
        # 2. Count how many elements are NOT equal to M.
        # These are the elements that must be changed.
        operations_count = 0
        for element in nums:
            if element != minimum_value:
                operations_count += 1
                
        return operations_count

# --- Alternative concise approach using list comprehension/sum ---
# This is often cleaner in Python:
# return sum(1 for element in nums if element != minimum_value)
