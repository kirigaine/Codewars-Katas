# ***DESCRIPTION***
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# ***BASE CODE***
# def even_or_odd(number):

# ***CODE***
def even_or_odd(number):
    # If no remainder divided by 2, it's even. Else it's odd
    if number % 2 == 0:
        return "Even"
    return "Odd"