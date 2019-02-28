
###########################################################################
#####
##### Trie, in Python 3

##### What is a TRIE
''' To answer this question let's see for what it was made 
'''

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
    # Because maybe
    self.end_of_word = False
    self.is_capital_letter = False

class Trie(object):

  def __init__(self):
    self.root = self.get_node()
    # root = self.get_node()
    self.index_of_letter = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, 
                            "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, 
                            "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, 
                            "w":22, "x":23, "y":24, "z":25}
    
    #TODO: If the word is a capital letter change the property of is_capital_letter 
    #      to true, 
    self.change_from_not_capital_letter_ = 

  def get_node():
    return Node()

  def add_word(self, word):
    # BIG(O)Notation:
    # Expected Time Complexity: O(k) => Where 'k' is the average lenght of a string
    # Expected Space Complexity: O(number of possible values??)
    # Current Time Complexity: ???
    # Current Space Complexity: ???
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

  def lenght_of_string_over_50()
    # if the lenght of the word is over 50 say it's to long to add

  def contains(self, word):
    """Return True if the trie constains the given word, otherwise False."""
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))
    # Current Time Complexity: ???
    # Current Space Complexity: ???
    
    # Notes
    #  * It stores for every position in the array a pointer to the next
    #    place where the continuation of the word follows, also given that 
    #    you are searching for the lenght of the word it's not neccesary 
    #    to go further than that
    #  * Remenber that there are only 
    #  * Every character is stored in a different level of the word
    
    # Approach:
    #  * You have find the looked after word
    #  * There will only be as many children has the longest word
    #  * If the word exist at the end of it, the complete word must be there and
    #    the node property end of word would be true

    # THINK OF ADDING something 

    # Mark the place where to begin at
    starting_point = self.root
    # The lenght of the word is has many levels ahs you have to search for
    number_of_levels = len(word)
    # Iterate through has many level has long the word is
    for each_level in range(number_of_levels):
      # the index is the 

      index = self.children[i]
      index_of_letter(word[])
      if starting_point.children[index] is None:
        return False
      if each_level[index].end_of_word == True:
        return True
  
def main():
  keys = ['hello', 'palabra', 'hell', 'palabrota', 'helado', 'ice', 'icecream', 'cream', 'palo',
          'hegel', 'putrido', 'putrid', 'puno', 'pork', 'cork']

  t = Trie() #Making a trie object

  for key in keys:
    t.add_word(key)
  print("Our Trie %s" %(t))

if __name__ == '__main__':
  main()