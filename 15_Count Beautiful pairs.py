# Count Beautiful Pairs

# You have an array AA of NN integers.
# A pair of indices (i,j)(i,j) is called Beautiful if Ai=Aj2Ai​=Aj2​ and 1≤i<j≤N1≤i<j≤N.
# Count the number of Beautiful Pairs in the given array.
# Task
# Try to solve this problem in N2N2 time complexity.
  
# Input Format
# The first line of the input contains a single integer NN, denoting the length of array AA.
# The second line of the input contains NN space-separated integers A1,A2,…,ANA1​,A2​,…,AN​ — denoting the array AA.

# Output Format
# Output the number of Beautiful Pairs in the given array AA.

# Constraints
# 2≤N≤1032≤N≤103
# 1≤Ai≤1041≤Ai​≤104


#Cook your dish here
CODE = 

n = int(input())
arr = list(map(int, input().split()))

res = 0 
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j] * arr[j]:
            res += 1
            
print(res)



