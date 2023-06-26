# ***DESCRIPTION***
# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

# ***BASE CODE***
# def string_to_array(s):
    # # your code here
    
# ***CODE***
def string_to_array(s):
    # Use string split with delimiter ' '
    return s.split(" ")