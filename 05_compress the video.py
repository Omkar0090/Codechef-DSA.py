Compress the Video
# Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.
# Chef's video has NN frames initially. The value of the ithith frame is AiAi. Chef can do the following type of operation any number of times:

# * Choose an index ii (1≤i≤N)(1≤i≤N) such that the value of the ithith frame is equal to the value of either of its neighbors and remove the ithith frame.
# Find the minimum number of frames Chef can achieve.
# Input Format

# * First line will contain TT, the number of test cases. Then the test cases follow.
# * The first line of each test case contains a single integer NN - the number of frames initially.
# * The second line contains NN space-separated integers, A1,A2,…,ANA1,A2,…,AN - the values of the frames.
# Output Format
# For each test case, output in a single line the minimum number of frames Chef can achieve.
# Constraints

# * 1≤T≤10001≤T≤1000
# * 1≤N≤1051≤N≤105
# * 1≤Ai≤1061≤Ai≤106
# * Sum of NN over all test cases does not exceed 2⋅1052⋅105.

CODE = 

# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # count unique consecutive elements
    count = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            count += 1
    
    print(count)
