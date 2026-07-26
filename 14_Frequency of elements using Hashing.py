Frequency of elements using Hashing

# You are given an integer NN and an array containing NN integers.
# For each element in the array, you have to output its frequency in the array using Hashing.
# The frequency of an element in the array tells how many times it occurs in the array.
# Input Format

# * The first line of input will contain a single integer TT, denoting the number of test cases.
# * Each test case consists of multiple lines of input.
# * The first line of each test case contains one integer NN denoting the number of elements in the array.
# * The next line contains NN space separated integers, denoting the elements in the array.

# Output Format
# For each test case, output NN space separated integers denoting the frequency of each element of the array.
# Constraints

# * 1≤N≤1051≤N≤105
# * 1≤max(A)≤1001≤max(A)≤100

# Sample 1:
# Input
# Output
# 3
# 10
# 1 2 1 2 1 3 4 1 2 3
# 5 
# 1 1 1 1 1
# 5
# 1 2 1 2 1
# ```
# ```
# 4 3 4 3 4 2 1 4 3 2
# 5 5 5 5 5
# 3 2 3 2 3
# ```
# Explanation:
# Test Case 1: In this array 11 occurs 44 times, 22 occurs 33 times, 33 occurs 22 times and 44 occurs 11 times.
# Test Case 2: In this array 11 occurs 55 times.
# Test Case 3: In this array 11 occurs 33 times and 22 occurs 22 times.

CODE = 

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx]); idx += 1
    results = [] 
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = data[idx:idx + n]
        arr = list(map(int, arr))
        idx += n
        # Step 1: Find max element -> determines Hash array size
        M = max(arr)
        # Step 2: Declare Hash array of size M+1, initialized to 0
        Hash = [0] * (M + 1)
        # Step 3: Count frequency of each element -> O(N)
        for num in arr:
            Hash[num] += 1
        # Step 4: Build output by mapping each element to its frequency -> O(N)
        ans = [str(Hash[num]) for num in arr]
        results.append(" ".join(ans))
    print("\n".join(results))
if __name__ == "__main__":
    main()
