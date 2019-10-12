"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""

sum = 0
sum_squares = 0
for x in range(1, 101):
    sum += x
    sum_squares += (x ** 2)
    print(str(x))
sum = sum ** 2
print("Sum Squares: " + str(sum_squares))
print("Squared Sum: " + str(sum))
print("Result: " + str(sum - sum_squares))