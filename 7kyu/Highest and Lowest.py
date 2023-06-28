# ***DESCRIPTION***
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# ***BASE CODE***
# def high_and_low(numbers):
    # # ...
    # return numbers
    
# ***CODE***
def high_and_low(numbers):
    # Split the string at spaces and convert array values to integer values
    new = [int(value) for value in numbers.split()] 
    # Call max and min function and return values in format
    return "%d %d" % (max(new),min(new))
    
# Before refactoring
# def high_and_low(numbers):
    # # Split the string at spaces
    # new = numbers.split()
    # # Convert array values to integer values
    # for i in range(0,len(new)): new[i] = int(new[i])
    # # Call max and min function and return values in format
    # return "%d %d" % (max(new),min(new))