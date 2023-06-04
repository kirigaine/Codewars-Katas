# ***DESCRIPTION***
# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]
#
# ***BASE CODE***
# def reverse_seq(n):
#    pass

def reverse_seq(n):
    # Check for base case
    
    if n>0:
        # Append n to array, subtract 1 from neach iteration
        x = []
        while n > 0:
            x.append(n)
            n=n-1
            
        return x
    pass