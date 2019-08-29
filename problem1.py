# näive, brute force approach
total = 0
for i in range(1,1000):
    if not i % 3 or not i % 5:
        total += i
print(total)

# pythonic list comprehension brute force
print(
    sum(
        [x for x in range(1000) if not x % 3 or not x % 5]
    )
)

# O(1) approach
# count all multiples of 3 and 5, subtract out double-counted multiples of 15
threes   = (1000 - 1) // 3 # double division is the integer division
fives    = (1000 - 1) // 5
fifteens = (1000 - 1) // 15
print (3 * threes   * (threes    + 1) / 2
     + 5 * fives    * (fives     + 1) / 2
    - 15 * fifteens * (fifteens  + 1) / 2
)