Convert string to number

You are given a string that represents a positive number. Your task is to write a program that converts this string into its numerical equivalent without using any in-built parsing, conversion libraries, or direct type casting methods. The string will not contain any leading zeros, decimals, or any non-numeric characters.
Complete the function stringToNumber in the IDE
Input Format

* The first line contains a single integer, T, the number of test cases.
* The following T lines each contain a single string, S, representing the number.

CODE = 

def string_to_number(s):
    num = 0
    for char in s:
        num = num * 10 + (ord(char) - ord('0'))
    return num
