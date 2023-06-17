# ***DESCRIPTION***
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# ***BASE CODE***
# def get_count(sentence):
    # pass
    
# ***CODE***
def get_count(sentence):
    # Define vowels
    vowels = ['a','e','i','o','u']
    total = 0
    # Iterate and count
    for vowel in vowels: total += sentence.count(vowel)
    return total