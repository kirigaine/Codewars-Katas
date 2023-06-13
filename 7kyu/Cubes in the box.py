# ***DESCRIPTION***
# Cubes in the box
# Your job is to write a function f(x,y,z) to count how many cubes of any size can fit inside a x*y*z box. For example, a 2*2*3 box has 12 1*1*1 cubes, 2 2*2*2 cubes, so a total of 14 cubes in the end. See the animation below for a visual description of the task!

# Notes:
# x,y,z are strictly positive and will not be too big.

# https://i.ibb.co/KXzMQkC/cube.gif

# ***BASE CODE***
# def f(x, y, z):
    # ...

# ***CODE***

# In order to be a cube, all dimensions must be the same (e.g. 1*1*1 or 3*3*3 etc.)

def f(x, y, z):
    # Account for 1*1*1 cubes first and set to total
    total = x * y * z
    if min([x,y,z]) > 1:
        for value in range(2,min([x,y,z])):
            # Figure out mathematically how to account for duplicate use cubes
            #total += total_cubes
            pass
    return total