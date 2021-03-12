# Date: March 11 2021
# Euler 1: Multiples of 3 and 5
# Problem: If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum1 = 0
sum2 = 0
for num in range(3,1000):
    if num % 3 == 0:
        sum1 += num
    if num % 5 == 0 and num % 3 != 0:
        sum2 += num

total = sum1 + sum2

print(total)