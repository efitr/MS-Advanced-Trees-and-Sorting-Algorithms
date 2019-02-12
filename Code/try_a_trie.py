
###########################################################################
#####
##### Trie, in Python 3

##### WTF is a TRIE
'''' To answer this question let's see for what it was made ''''

##### For what it was made
''' It's role is that of organizing letters in the alphabet.
    You use it to complete words, autocorrector is a very good one '''

##### How it works
''' It's a series of linked list that all connect to an empty node '''

##### Traits
''' 
  *  It is has long as there are values variations
  *  Tends to begin on an empty string
  *  Both the value and the value reference could be empty
  *  Each node contains an array of references/links, it is defined 
'''

#Every node represents one letter of some prefix
class Node(object):
  def __init__(self):
    self.children = [None]*26
    self.end_of_word = False

class Trie(object):

  def __init__(self):
    self.root = self.get_node()

  def get_node():
    return Node()
  
  # This is meant to identify if the word is already stored
  def already_on_trie(self, key):
  #
  def add_word(self, key):
    
    #
    if node.already_on_trie() == False:
      return 

  def search(self, key):

  def delete():

def main():
  keys = ['hello', 'palabra', 'hell', 'palabrota', 'helado', 'ice', 'icecream', 'cream', 'palo',
          'hegel', 'putrido', 'putrid', 'puno', 'pork', 'cork']

  t = Trie()

  for key in keys:
    t.add_word(key)

if __name__ == '__main__':
  main()