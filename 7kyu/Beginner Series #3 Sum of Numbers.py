# ***DESCRIPTION***
#Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

#Note: a and b are not ordered!

#Examples (a, b) --> output (explanation)
#(1, 0) --> 1 (1 + 0 = 1)
#(1, 2) --> 3 (1 + 2 = 3)
#(0, 1) --> 1 (0 + 1 = 1)
#(1, 1) --> 1 (1 since both are same)
#(-1, 0) --> -1 (-1 + 0 = -1)
#(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
#Your function should only return a number, not the explanation about how you get that number.

# ***BASE CODE***
#def get_sum(a,b):
    #good luck!
    
# ***CODE***

def get_sum(a,b):
    
    # Account for edge case
    
    if a is b: return a

    # Assure consistent format

    if a > b:
        temp = a
        a = b
        b = temp
        
    # Create sum and interate from a to b while adding
        
    sum = 0
    while a <= b:
        sum += a 
        a += 1
        
    return sum

    # Create the range of numbers (account for top end exclusivity with +1) and add all values to returned sum
        
    #x = range(a,b+1)
    #sum = a
    #for n in x:
    #    sum += n
    #return sum