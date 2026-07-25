Frequency of each element in the array

# You are given an integer 
# N and an array containing 
# N integers.
# For each element in the array you have to output it's frequency in the array.
# Frequency of an element in the array tells how many times it occurs in the array.

# Iterate over each element in the array and count the frequency of that element using another loop then print the frequency for each element in the array.

# Input Format
# The first line of input will contain a single integer 
# T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains one integer 
# N denoting the number of elements in the array.
# The next line contains 
# N space separated integers, denoting the elements in the array.
# Output Format
# For each test case, output 
# N space separated integers denoting the frequency of each element of the array.

# Constraints

# 1≤T≤1001≤T≤100
# 1≤N≤1001≤N≤100
# 1≤Ai≤101≤Ai≤10

# Explanation:
# Test Case 1: In this array 11 occurs 44 times, 22 occurs 33 times, 33 occurs 22 times and 44 occurs 11 times.
# Test Case 2: In this array 11 occurs 55 times.
# Test Case 3: In this array 11 occurs 33 times and 22 occurs 22 times.

CODE = 

# cook your dish here
from collections import Counter

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        freq = Counter(arr)  # builds hash map of value -> frequency
        
        ans = [str(freq[num]) for num in arr]
        results.append(" ".join(ans))
    
    print("\n".join(results))

solve()
