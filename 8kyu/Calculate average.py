# ***DESCRIPTION***
#Write a function which calculates the average of the numbers in a given list.

#Note: Empty arrays should return 0.

# ***BASE CODE***
#def find_average(numbers):
    # your code here
#    pass

# ***CODE***

def find_average(numbers):
    # Account for edge case
    length = len(numbers)
    if length == 0: return 0
    
    # Iterate and sum all numbers. Divide by length for average
    sum = 0
    for num in numbers:
        sum += num
    return sum / length