# ***DESCRIPTION***
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# ***BASE CODE***
# def likes(names):
    # # your code here
    # pass
    
# ***CODE***
def likes(names):
    
    # Get length to determine format
    length = len(names)
    
    # Use string variable insertion and a switch case to give proper response
    match length:
        case 0:
            return "no one likes this"
        case 1:
            return "%s likes this" % names[0]
        case 2:
            return "%s and %s like this" % (names[0], names[1])
        case 3:
            return "%s, %s and %s like this" % (names[0], names[1], names[2])
        case _:
            # Minus 2 from length to account for 2 names listed
            return "%s, %s and %d others like this" % (names[0], names[1], length-2)