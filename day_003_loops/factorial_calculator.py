#/* Factorial Calculator */

# Factorial Rule
# 0! = 1
# 1! = 1
# 2! = 2 x 1
# 3! = 3 x 2 x 1
# 4! = 4 x 3 x 2 x 1
# .    .   .   .   .
# .    .   .   .   .
# .    .   .   .   .
# n! = n x (n-1) x (n-2)...... x 3 x 2 x 1
#-----------------------------------------------------

num = int(input(" Enter the number : "))

fact = 1

if num < 0:
    print(" Invalid input! Enter only positive numbers.")

elif num == 0:
        print(fact)

elif num > 0:
    for i in range(num, 0, -1):
        # print(fact)-- Checking calue of fact
        # print(f"Value of I is: {i}")-- Checking value of i
        fact = fact * i
    print(f" The factorial of {num} is :", fact)
