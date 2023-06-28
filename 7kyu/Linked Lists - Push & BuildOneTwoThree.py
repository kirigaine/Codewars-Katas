# ***DESCRIPTION***
# Linked Lists - Push & BuildOneTwoThree

# Write push() and buildOneTwoThree() functions to easily update and initialize linked lists. Try to use the push() function within your buildOneTwoThree() function.

# Here's an example of push() usage:

# var chained = null
# chained = push(chained, 3)
# chained = push(chained, 2)
# chained = push(chained, 1)
# push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null
# The push function accepts head and data parameters, where head is either a node object or null/None/nil. Your push implementation should be able to create a new linked list/node when head is null/None/nil.

# The buildOneTwoThree function should create and return a linked list with three nodes: 1 -> 2 -> 3 -> null

# Related Kata in order of expected completion (increasing difficulty):
 # Linked Lists - Push & BuildOneTwoThree
 # Linked Lists - Length & Count
 # Linked Lists - Get Nth Node
# Linked Lists - Insert Nth Node
# Linked Lists - Sorted Insert
# Linked Lists - Insert Sort
# Linked Lists - Append
# Linked Lists - Remove Duplicates
# Linked Lists - Move Node
# Linked Lists - Move Node In-place
# Linked Lists - Alternating Split
# Linked Lists - Front Back Split
# Linked Lists - Shuffle Merge
# Linked Lists - Sorted Merge
# Linked Lists - Merge Sort
# Linked Lists - Sorted Intersect
# Linked Lists - Iterative Reverse
# Linked Lists - Recursive Reverse

# Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.

# I'm aware that there are better ways to create linked lists (class methods, reference pointers, etc.), but not all languages have the same features. I'd like to keep the basic API consistent between language translations for this kata.

# ***BASE CODE***
# class Node(object):
    # def __init__(self, data):
        # self.data = data
        # self.next = None
    
# def push(head, data):
    # # Your code goes here.
  
# def build_one_two_three():
    # # Your code goes here.
    
# ***CODE***
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    # Create a new node, set its next to head
    new_node = Node(data)
    new_node.next = head 
    return new_node
    
def build_one_two_three():
    # Build a linked list in reverse with three nodes
    chained = None
    for value in range(3,0,-1): chained = push(chained, value)
    return chained
