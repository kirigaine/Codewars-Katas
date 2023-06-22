# ***DESCRIPTION***
# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

# ***BASE CODE***
# def zeros(n):
    # return 0
    
# ***CODE***
import math

def zeros(n):
    # Account for edge case
    if n == 0: return 0
    # Follow formula, return sum of range
    return sum(math.floor(n/5**k) for k in range(1,math.floor(math.log10(n) / math.log10(5))+1))

# ***CODE BEFORE REFACTORING***
# import math

# def zeros(n):
    # if n == 0: return 0
    # total = 0
    # for k in range(1,math.floor(math.log10(n) / math.log10(5))+1)
        # total += math.floor(n/5**k)
    # return total