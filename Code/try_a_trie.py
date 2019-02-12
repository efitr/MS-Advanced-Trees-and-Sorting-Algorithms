
###########################################################################
#####
##### Trie, in Python 3

##### WTF is a TRIE
'''' To answer this question let's see for what it was made ''''

##### For what it was made
''' It's role is that of organizing letters in the alphabet '''

##### How it works
''' It's a series of linked list that all connect to an empty node '''

##### Traits
''' 
  *  It is has long as there are values variations
  *  Tends to begin on an empty string
  *  Both the value and the value reference could be empty
  *  Each node contains an array of references/links, it is defined by the links index
  *  Nodes can contain two things a value which might be null and references to a child node that might also be null
  *  It has an index and it's lenght depends on the possible number of variations of what's getting on it
'''

##### Confusion
'''
Is it that because of it's nature it relies on having has max lenght the total number of possible variations, but then wouldn't it 
become a humongous amount of possible nodes, also it seems that the index is the element that makes this be able to happen
'''
