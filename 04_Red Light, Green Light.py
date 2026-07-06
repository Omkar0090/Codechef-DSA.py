Red Light, Green Light

# “You won’t get caught if you hide behind someone.”
# Sang-Woo advises Gi-Hun to hide behind someone to avoid getting shot.
# Gi-Hun follows Sang-Woo's advice and hides behind Ali, who saved his life earlier. Gi-Hun and Ali both have the same height, KK. Many players saw this trick and also started hiding behind Ali.
# Now, there are NN players standing between Gi-Hun and Ali in a straight line, with the ithith player having height HiHi. Gi-Hun wants to know the minimum number of players who need to get shot so that Ali is visible in his line of sight.
# Note:

# * Line of sight is a straight line drawn between the topmost point of two objects. Ali is visible to Gi-Hun if nobody between them crosses this line.
# * Even if there are some players who have the same height as that of Gi-Hun and Ali, Ali will be visible in Gi-Hun's line of sight.
# * Gi-Hun and Ali have the same height.
# Input Format

# * The first line of input contains a single integer TT, denoting the number of test cases. The description of TT test cases follows.
# * The first line of each test case contains two space-separated integers NN and KK, denoting the total number of players between Gi-Hun and Ali and the height of both of them respectively.
# * The second line of each test case contains NN space-separated integers, denoting the heights of the players between Gi-Hun and Ali.
# Output Format
# For each test case, output in a single line the minimum number of players who need to get shot so that Ali is visible in Gi-Hun's line of sight.
# Constraints

# * 1≤T≤1051≤T≤105
# * 1≤N≤1051≤N≤105
# * 1≤K≤1061≤K≤106
# * 1≤Hi≤1061≤Hi≤106 for every 1≤i≤N1≤i≤N.
# * The sum of NN across all test cases does not exceed 5⋅1055⋅105.

CODE = 

# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(sum(1 for h in arr if h > k))
