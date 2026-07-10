Reverse Words in a String

# You are given a string S consisting of English letters (uppercase and lowercase), digits, and spaces ' '. The string may contain leading or trailing spaces, or multiple spaces between words.

# Your task is to reverse the order of the words in the string. A word is defined as a sequence of non-space characters.

# The resulting string should:
# Contain words in reversed order.
# Have only single spaces separating words.
# Not contain leading or trailing spaces.

# Function Name
# reverseWords – This function reverses the order of words in a given string while ensuring that words are separated by exactly one space and there are no leading or trailing spaces.

# Parameters
# s : A string consisting of English letters (uppercase and lowercase), digits, and spaces ' '.

CODE = 

def reverseWords(s: str) -> str:
    chars = list(s)
    n = len(chars)

    # Step 1: Reverse the entire string
    chars.reverse()

    # Step 2: Reverse each word
    start = 0
    for i in range(n + 1):
        if i == n or chars[i] == ' ':
            left, right = start, i - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            start = i + 1

    # Step 3: Remove extra spaces in-place
    idx = 0
    i = 0
    while i < n:
        # skip spaces
        while i < n and chars[i] == ' ':
            i += 1
        if i >= n:
            break

        # copy word
        while i < n and chars[i] != ' ':
            chars[idx] = chars[i]
            idx += 1
            i += 1

        # skip spaces after word
        while i < n and chars[i] == ' ':
            i += 1

        # add space if another word exists
        if i < n:
            chars[idx] = ' '
            idx += 1

    return ''.join(chars[:idx])

------------------------------------------------------------------------------------------

s = input()

def reverseWords(s):
    words = s.split()
    return ' '.join(reversed(words))

print(reverseWords(s))
