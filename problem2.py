"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def naive_approach():
    prev, curr = 1, 2
    sum = 0

    while (curr <= 4000000):
        if not curr % 2:
            sum += curr
        curr = curr + prev
        prev = curr - prev
    print("Brute force approach: ", sum)

# on the premise that each third number of the fibonacci sequence is even:
def nuanced_approach():
    x, y = 1, 1
    sum = 0
    while (sum < 4000000):
        sum += (x + y)
        new_y = x + 2 * y
        new_x = 2 * x + 3 * y
        x, y = new_y, new_x
    print("Nuanced approach:     ", sum)

naive_approach()
nuanced_approach()