import math

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
# classic primality test
def is_prime(val):
	if val < 2: # zero and one are not prime
		return False
	if val == 2 or val == 3: # two and three are
		return True
	if val % 2 == 0: # rule out all evens
		return False
	if val % 3 == 0: # rule out multiples of 3
		return False
	if val < 9: # between zero and nine, all that's left is 5 and 7, both pri,es
		return True
	# now test for all natural multiples
	max_prime = int(math.ceil(math.sqrt(val)))
	test = 5;
	while (val > test):
		if val % test == 0:
			return False
		if val % test + 2 == 0:
			return False
		# all primes greater than 6 are of the form 6k ± 1
		test = test + 6
	return True

def is_factor(val, test):
	return (val / test) % 1 == 0

val = 600851475143							# the original input
max_factor = int(math.ceil(math.sqrt(val)))	# no need to test numbers larger than this
largest_prime_factor = -1
for test in range(1, max_factor):
	if is_factor(val, test):
		print(str(test) + " is a factor of " + str(val))
		if is_prime(test):
			print(str(test) + " is prime!")
			largest_prime_factor = test

print("Largest prime factor found was " + str(largest_prime_factor))