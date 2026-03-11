#/* Multiplication Table Generator */

# Multiplication Rule
#
# n x 1  =  1n
# n x 2  =  2n
# n x 3  =  3n
# n x 4  =  4n
# n x 5  =  5n
# n x 6  =  6n
# .   .     . 
# .   .     .
# .   .     .
# .   .     .
# n x 10 = 10n
# .   .  =   . 
# .   .  =   .
# .   .  =   .
# n   n  =   nn
#----------------------------------------------------------------------------

# Table limit is 10
"""
num = int(input(" Enter the number to generate its multiplication table : "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

"""
# Table limit is "n"(user input)

num = int(input(" Enter the number to generate its multiplication table : "))
n   = int(input(" Enter the table limit : "))

for i in range(1, n+1):
    print(f"{num} x {i} = {num*i}")




