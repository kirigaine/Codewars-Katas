# ***DESCRIPTION***
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1^2 + 2^2 + 2&2 = 9.

# ***BASE CODE***
#def square_sum(numbers):
    # your code here
    
# ***CODE***
def square_sum(numbers):
    sum = 0
    # Iterate and add square to sum, return sum after loop
    for number in numbers:
        sum += number * number
    return sum