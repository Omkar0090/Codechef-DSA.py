Hashing Function Example
# We can use multiple Hash Functions.
# One simple example of a Hash function is the modulo operator %% (We had used this to explain how hashing works).
# We can define the Hash function as f(x)=xf(x)=x %% MM. Here MM is an arbitrary integer.
# The output range of this function will be [0,M−1][0,M−1].
# So we need to choose MM such that we are able to index all the values from 00 to M−1M−1.
# We can safety make MM as large as 106106.
# Also we will try to choose MM as a prime number so that the output is distributed evenly.
# Let's fix MM as 999983999983 for now - it's a prime number and is small enough to be indexed.
# Task
# Run the code in the IDE and check the output.
# Sample 1:
# Input
# Output

# ```
# 13
# 1000000000
# 342561313
# 1341234
# 523151339
# ```


# ```
# x = 13, f(x) = 13
# x = 1000000000, f(x) = 17000
# x = 342561313, f(x) = 567127
# x = 1341234, f(x) = 341251
# x = 523151339, f(x) = 160230
# ```

CODE = 

def f(x):
    return x % 999983

for i in range(5):
    x = int(input())
    print(f"x = {x}, f(x) = {f(x)}")


Explain this
