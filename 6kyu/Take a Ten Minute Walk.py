# ***DESCRIPTION***
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

# ***BASE CODE***
# def is_valid_walk(walk):
    # #determine if walk is valid
    # pass
    
# ***CODE***
def is_valid_walk(walk):
    time = x = y = 0
    for direction in walk:
        # Stop the calculations if we go over ten minutes, there's no point
        if time > 10: break
        # Affect x and y based on direction
        if direction == 'n': y += 1
        elif direction == 's': y += -1
        elif direction == 'e': x += 1
        elif direction == 'w': x += -1
        time +=1
    # If we're at starting point (0,0) and have 10 or less minutes spent, it's a good walk
    if x == y == 0 and time <= 10: return True
    # Otherwise, bad walk return false
    return False