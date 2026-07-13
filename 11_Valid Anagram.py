Valid Anagram

# You are given two strings 
# s and t. Your task is to determine whether t is an anagram of s.

# An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly the number of times it is used.
# Function Declaration
# Function Name
# isAnagram – This function checks whether one string is an anagram of another string.

# Parameters
# s : A string representing the original word.
# t : A string to be checked as an anagram of s.
# Return Value
# Returns 
# true if t is an anagram of s.
# Returns 
# false otherwise.

CODE =  

# write your code here...
    
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 'a' to 'z'

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True
