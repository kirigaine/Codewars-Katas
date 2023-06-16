# ***DESCRIPTION***
# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

 # *
# ***
 # *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:

  # *
 # ***
# *****
 # ***
  # *
# ...that is:

# "  *\n ***\n*****\n ***\n  *\n"

# ***BASE CODE***
# def diamond(n):
    # # Make some diamonds!
    # return "*"
    
# ***CODE***
from math import ceil

def diamond(n):
    # Account for edge cases
    if n % 2 == 0 or n <= 0 or n is None: return None
    parts = []
    # Solve half of the diamond
    for num in range(1,ceil(n/2)):
        spaces = abs(ceil(n/2)-num)
        parts.append(" "*spaces + "*"*(n-(spaces*2)) + "\n")
        
    # Return the half, the middle with no spaces, and the first half read in reverse
    return "".join(parts + ["*"*n,"\n"] + parts[::-1])
    
# Solved without reverse reading a list
    
# def diamond(n):
    # # Account for edge cases
    # if n % 2 == 0 or n <= 0 or n is None: return None
    # string = ""
    # for num in range(1,n+1):
        # spaces = abs(ceil(n/2)-num)
        # stars = n-(spaces*2)
        # string += " "*spaces + "*"*stars
    # return string