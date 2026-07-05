Find maximum in an Array

CODE = 

# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    maximum = A[0]
    
    for num in A:
        if num > maximum:
            maximum = num
            
    print(maximum)
