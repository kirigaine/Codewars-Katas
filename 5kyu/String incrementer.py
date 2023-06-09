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
    parts = re.split(r'([0-9])',strng,1)
    if len(parts) > 1:
        # UNFINISHED, ACCOUNT FOR LEFT AND RIGHT JUSTIFICATION OF ZEROS. NEED ZFILL()?
        return parts[0] + str((int(parts[1] + parts[2]) + 1))
    return parts[0]
    
print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar100"))