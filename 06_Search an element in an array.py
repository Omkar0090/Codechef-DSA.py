Search an element in an array

CODE = 

# cook your dish here


# def solve(N, X, A):
#     return "YES" if X in A else "NO"
    
    
def solve(N, X, A):
    try:
        A.index(X)
        return "YES"
    except:
        return "NO"
