# ***DESCRIPTION***
#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#Examples:

#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#spinWords( "This is a test") => returns "This is a test" 
#spinWords( "This is another test" )=> returns "This is rehtona test"

# ***BASE CODE***
#def spin_words(sentence):
    # Your code goes here
#    return None

# ***CODE***
def spin_words(sentence):
    
    # Split the sentence into a list of strings, begin constructing new sentence
    
    words = sentence.split(" ")
    new_sentence = ""
    
    # Iterate each word in list, reverse if necessary. Append to new sentence
    for word in words:
        if len(word) >= 5: new_sentence += word[::-1] + " "
        else: new_sentence += word + " "
                
    # Remove space from end
    return new_sentence.strip()