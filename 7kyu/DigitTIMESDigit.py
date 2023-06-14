# ***DESCRIPTION***
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

# ***BASE CODE***
# def square_digits(num):
    # # Your code here
    
# ***CODE***
def square_digits(num):
    # Check input type
    if not isinstance(num, int): return None
    # Create an empty list for new numbers
    new_number = []
    for number in str(num):
        # Iterate and append squared (cast) value of int
        new_number.append(str(pow(int(number),2)))
    # Join list and return
    return int("".join(new_number))