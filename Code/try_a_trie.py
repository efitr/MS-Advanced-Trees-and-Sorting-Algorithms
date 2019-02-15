
###########################################################################
#####
##### Trie, in Python 3

##### What is a TRIE
'''' To answer this question let's see for what it was made 
''''

##### For what it was made
''' It's role is that of organizing letters in the alphabet.
    You use it to complete words, autocorrector is a very good use example of 
    a trie in action
'''

##### How it works
''' It's a series of linked list that all connect to an empty node '''

##### Traits
''' 
    * It is has long as there are values variations
    * Tends to begin on an empty string
    * Both the value and the value reference could be empty
    * Each node contains an array of references/links, it is defined 
'''

##### Big (O) notation

#Every node represents one letter of some prefix
class Node(object):
  def __init__(self):
    self.children = [None]*26
    # self.data = ""
    self.end_of_word = False

class Trie(object):

  def __init__(self):
    self.root = self.get_node()

  def get_node():
    return Node()
  
  # This is meant to identify if the word is already stored
  def already_on_trie(self, key):
    
    #if word is already on the trie, dont add it 
  
  # This function return the index position of the value that I'm currently trying to add
  def maps_element_to_alfabet_index(letter):
    index_of_letter = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9,
                       "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18,
                       "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
    return index_of_letter[letter]

  def add_word(self, word):
    # Using root from initializer
    node = self.root
    
    for letter in word:
      index = self.maps_element_to_alfabet_index(letter)
      # Possible values
      # Coudl ahve a node
      if node.children[index] is None:
        # Create a new node for that index
        new_node = self.get_node()
        # 
        node.children[index] = new_node

        node = new_node
      else:
        node = node.children[index]
      
    node.end_of_word = True

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