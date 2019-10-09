"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def brute_force():
    answer_found = False
    guess = 2520
    while not answer_found:
        divisible = True
        for x in range(3, 20):
            if guess % x:
                divisible = False
                print(str(guess) + " is not divisible by " + str(x))
                break
        if divisible:
            answer_found = True
            print("\nResult: " + str(guess))
        else:
            guess = guess + 20

"""
More intelligent method: prime factorization.
"""
#brute_force() # takes awhile!
print("Result: " + str(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19))