# ***DESCRIPTION***
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# ***BASE CODE***
# def pig_it(text):
    # #your code here
    
# ***CODE***
import re

def pig_it(text):
    # Split the string/sentence along spaces
    sentence = re.split("\s", text)
    new_sentence = ""
    for word in sentence:
    # If string is just punctuation, append to new sentence
        if re.search("[!?.]",word):
            new_sentence += word
            continue
        # Pig latin-ify word and appened to new sentence
        new_sentence += word[1:] + word[0] + "ay "
    return new_sentence.strip()
