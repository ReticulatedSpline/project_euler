"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

answer_found = False
guess = 40
while not answer_found:
    divisible = True
    for x in range(1, 20):
        if guess % x:
            divisible = False
            break
    if divisible:
        answer_found = True
        print("\nResult: " + str(guess))
    else:
        guess = guess + 1