Largest and Second Largest

CODE = 

t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Find the absolute maximum element
    m1 = max(a)
    # Initialize m2 (the second distinct maximum) to a small value (0 is fine given constraints A_i >= 1)
    m2 = 0
    # Iterate through the array to find the largest element that is NOT m1
    for x in a:
        if x != m1:
            m2 = max(m2, x)   
    print(m1 + m2)
    t -= 1
