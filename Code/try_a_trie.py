
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

  def __init__(self, words=[]):
    self.root = Node()
    for word in words:
      if self.contains(word) is False:
        self.add_the_word_letter_by_letter(word)

  def get_index(self, letter):
    # print(letter)
    return ord(letter.lower())-ord('a')
  
  def get_letter(self, index):
    return node.children[index]

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
    # The lenght of the word is has many levels has you have to search for
    for letter in word:
      index = self.get_index(letter)

      if node.children[index] is None:
        return False

      node = node.children[index]

    if node.end_of_word == True:
      return True
    # I don't think I actually need this
    return False

  # This will go through every node.children and do something when there is a node in an 
  # index of the 
  def _get_to_every_node_on_children(self, python3_list):
    # Purpose:
    #   * Go through every element in the list and if there is a node call _get_string_without_prefix
    for node in range(len(python3_list)):
      if node != None:
        # I need to get an index of where the node is 
        # _get_string_without_prefix this recursively should keep on going deeper 
      
      
      if self.end_of_word == True:
        # 

        _add_word_with_prefix_to_list()

  # Remenber I'm working with indexes, I'm always only working with the index,
  # because if in the index there is a node, a word has been added 
  # I have to get until the prefix has been found
  # Remenber the property of is_end_of_word
  def _get_string_without_prefix(self, index): # What I'm getting here
    # Purpose:
    #   * Get the remaining of the word that gets made from the prefix
    # Approach:
    #   * First make

    # This only needs from the prefix get all the words that have it
    # Every word that has this prefix, has this prefix and the property is true,
    # How could I use is_end_of_word
    # I can use this function so in the node at the end of the prefix, for everyword it finds
    # on that node recursively get every letter until the property is found

     # everytime the property is_end_of_word is true
    # This is using the node from seach to 
    # First I need to get the letter
    word = ''

    if self.end_of_word == False:

      letter_to_append = self.get_letter(index_last_letter_of_prefix)

      # I have to think of where is the node
      current_letter = node[letter_to_append]
      _get_string_without_prefix(self, index_last_letter_of_prefix)

    word = '' + letter_to_append
      # get 
      # use string concatenation
      # use recursion on this function 

     # everytime it goes one layer deeper on recursion concatenate the letter at index
     # with the previous one

    # How exactly I'm saving this
    if self.end_of_word == True:
      return word_without_prefix

  # could this only be part of get_all_possible_words_with_prefix
  def _add_word_with_prefix_to_list(self, word, python3_list):
    # This will use _find_words_with_prefix
    if self.end_of_word is True:

    # for each word it finds with the determined prefix
    # This everytime find word with prefix gets to the property end of word, 
    # this appends the letter to the list

  # autocomplete program, finds all words with the prefix given 
  def get_all_possible_words_with_prefix(self, prefix):
    # Approach:
    #   * See if you have the prefix in your trie, if not return empty string
    #   * go iteratively until through every index that the node has
    #     last letter of the prefix
    #     has 
    # First, is the prefix on this, if not empty python3 list
    if self.contains(prefix) == False
      return []
    # Remenber that this has to concatenate the prefix to the word
    # After the previous step you add the word to the list
    
    # Second we are going from the first node until 
    node = self.root
    # The lenght of the word is has many levels has you have to search for

    # This is made thinking for when I make it be recursive to not do the first part many times
    if prefix_alone is prefix:


    for letter in word:
      index = self.get_index(letter)

      if node.children[index] is None:
        return False

      node = node.children[index]

    node = self.root




    #recursively i can start going into

    _get_to_every_node_on_children(self, node.children):


    # I have to find all the words with the prefix

    # I have to get until the node with the prefix

    # then call 


    _get_to_every_node_on_list(self, node.children)

    items_with_prefix = []
      # with _find_words_with_prefix you get each word with the prefix
      # with _add_word_with_prefix_to_list
      # I should add the word to the list

    return
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