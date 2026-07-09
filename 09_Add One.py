Add One

# You are given a large number NN. You need to print the number N+1N+1.
# Note: The number is very large and it will not fit in standard integer data type. You have to take the input as String and then manipulate the digits to convert it to N+1N+1.
# Input Format

# * The first line of the input contains a single integer TT - the number of test cases. The description of TT test cases follows.
# * The first line of each test case contains a single integer NN.
# Output Format

# * For each test case, print a single line string - the number N+1N+1.
# Constraints

# * 1≤T≤1001≤T≤100
# * 1≤N≤10200000−11≤N≤10200000−1
# * the sum of the number of digits of all NN in a single test file does not exceed 4⋅1054⋅105

CODE = 

# cook your dish here
def addOne(s):
    s = list(s)
    carry = 1
    
    for i in range(len(s)-1, -1, -1):
        digit = (ord(s[i]) - ord('0')) + carry
        s[i] = str(digit % 10)
        carry = digit // 10
        if carry == 0:
            break
    
    if carry:
        s.insert(0, '1')
    
    return ''.join(s)

t = int(input())
for _ in range(t):
    n = input()
    print(addOne(n))
