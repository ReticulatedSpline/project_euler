"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# brute force approach
def is_palindrome(val):
    string = str(val)
    if string[0] != string[-1]:
        return False
    for i in range(1, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

largest_palindrome = 0
for x in range(100, 999):
    for y in range(100, 999):
        val = x * y
        if is_palindrome(val):
            if val > largest_palindrome:
                largest_palindrome = val
print("Largest found palindrome was " + str(largest_palindrome))
