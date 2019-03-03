
###########################################################################
#####
##### Trie, in Python 3

##### What is a TRIE
''' To answer this question let's see for what it was made 
'''

##### For what it was made
''' It's role is that of organizing letters in the alphabet.
    You use it to complete words, autocorrector is a very good use 
    example of a trie in action.
'''

##### How it works
''' On this scenario, every node an array of 26 spaces and a property end of word.
'''

##### Traits
''' * It is has long as there are values variations
    * Tends to begin on an empty string
    * Both the value and the value reference could be empty
    * Each node contains an array of references/links, it is defined 
'''

#Every node represents one letter of some prefix
class Node(object):
  def __init__(self):
    self.children = [None]*26
    self.end_of_word = False

class Trie(object):

  def __init__(self, items=[]):
    self.root = Node()
    for item in items:
      self.add_the_word_letter_by_letter(item)

  def get_index(self, letter):
    # print(letter)
    return ord(letter.lower())-ord('a')

  def add_the_word_letter_by_letter(self, word):
    # BIG(O)Notation:
    # Expected Time Complexity: O(k) => Where 'k' is the average lenght of a string
    # Expected Space Complexity: O(number of possible values??)
    # Current Time Complexity: ???
    # Current Space Complexity: ???
    # Using root from initializer

    node = self.root
    
    for letter in word:
      # This line should map the corresponding letter to it's index
      index = self.get_index(letter)
      # if on the node children (the list or python dynamic array with 26 spaces),
      # that space is empty
      if node.children[index] is None:
        # Create a new node for that index
        new_node = Node()

        node.children[index] = new_node

        node = new_node
      else:
        node = node.children[index]
      
    node.end_of_word = True

  def contains(self, word):
    """Return True if the trie contains the given word, otherwise False."""
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
    #  * You have to find the looked after word
    #  * There will only be as many children has the longest word
    #  * If the word exist at the end of it, the complete word must be there and
    #    the node property end of word would be true
    if (word == ''):
      return True
    # THINK OF ADDING something 
    # Mark the place where to begin at
    node = self.root
    # The lenght of the word is has many levels ahs you have to search for
    for letter in word:
      index = self.get_index(letter)

      if node.children[index] is None:
        return False
      node = node.children[index]

    if node.end_of_word == True:
      return True
    
    return False

  def _add_word_with_prefix_to_list(self, )

  # autocomplete program, finds all words with the prefix given 
  def search(self, prefix):
      if self.contains(prefix) == False
        return []

=

      # This should return a list with all the words that contain that 

def main():
  keys = ['hello', 'palabra', 'hell', 'palabrota', 'helado', 'ice', 'icecream', 'cream', 'palo',
          'hegel', 'putrido', 'putrid', 'puno', 'pork', 'cork']

  t = Trie() #Making a trie object

  for key in keys:
    t.add_word(key)
  print("Our Trie %s" %(t))

if __name__ == '__main__':
  main()