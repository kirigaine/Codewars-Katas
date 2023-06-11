# ***DESCRIPTION***
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

# ***BASE CODE***
# def increment_string(strng):
    # return strng
    
# ***CODE***
import re

def increment_string(strng):
    # Find all groups of numbers in string
    found = re.findall("[0-9]+",strng)
    # Account for edge case of no numbers
    if len(found) == 0: return strng+'1'
    
    # Access tail numbers of string, use that length to access everything else (word)
    numbers = found[len(found)-1]
    words = strng[:-len(numbers)]
    num_length = len(numbers)
    # Zfill length of leading zeroes
    new_numbers = str((int(numbers) + 1)).zfill(num_length)
    return words + new_numbers
    
    
    
# Function before finding learning input could have leading numbers 
    
# def increment_string(strng):
    # found = re.search("[0-9]+",strng)
    # if found is None: return strng+'1'
    # words = strng[0:found.start()]
    # numbers = strng[found.start():]
    # num_length = len(numbers)
    # new_numbers = str((int(numbers) + 1)).zfill(num_length)
    # return words + new_numbers
    # # print("Length: ", num_length)
    # # print(numbers)
    # # print(new_numbers)