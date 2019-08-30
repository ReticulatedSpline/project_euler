# brute force
prev = 1
curr  = 2
even_sum = 0

while (curr <= 4000000):
    if not curr % 2:
        even_sum += curr
    print(curr)
    curr = curr + prev
    prev = curr - prev
print("Sum of even fibonacci terms: ", even_sum)