#!python

from try_a_trie import Node, Trie
import random
import unittest

# class Node(object):
#   def __init__(self):
# class Trie(object):
#   def __init__(self):
#   def get_node():
#   def add_the_word_letter_by_letter(self, word):
#   def contains(self, word):


class TrieTest(unittest.TestCase):

    def test_get_index(self):
        trie = Trie()
        assert trie.get_index('a') == 0
        assert trie.get_index('b') == 1
        assert trie.get_index('c') == 2
        assert trie.get_index('d') == 3
        assert trie.get_index('e') == 4
        assert trie.get_index('f') == 5
        assert trie.get_index('g') == 6
        assert trie.get_index('h') == 7
        assert trie.get_index('i') == 8
        assert trie.get_index('j') == 9
        assert trie.get_index('k') == 10
        assert trie.get_index('l') == 11
        assert trie.get_index('m') == 12
        assert trie.get_index('n') == 13
        assert trie.get_index('o') == 14
        assert trie.get_index('p') == 15
        assert trie.get_index('q') == 16
        assert trie.get_index('r') == 17
        assert trie.get_index('s') == 18
        assert trie.get_index('t') == 19
        assert trie.get_index('u') == 20
        assert trie.get_index('v') == 21
        assert trie.get_index('w') == 22
        assert trie.get_index('x') == 23
        assert trie.get_index('y') == 24
        assert trie.get_index('z') == 25

    def test_get_letter(self):
        trie = Trie()
        assert trie.get_letter(0) == 'a'
        assert trie.get_letter(1) == 'b'
        assert trie.get_letter(2) == 'c'
        assert trie.get_letter(3) == 'd'
        assert trie.get_letter(4) == 'e'
        assert trie.get_letter(5) == 'f'
        assert trie.get_letter(6) == 'g'
        assert trie.get_letter(7) == 'h'
        assert trie.get_letter(8) == 'i'
        assert trie.get_letter(9) == 'j'
        assert trie.get_letter(10) == 'k'
        assert trie.get_letter(11) == 'l'
        assert trie.get_letter(12) == 'm'
        assert trie.get_letter(13) == 'n'
        assert trie.get_letter(14) == 'o'
        assert trie.get_letter(15) == 'p'
        assert trie.get_letter(16) == 'q'
        assert trie.get_letter(17) == 'r'
        assert trie.get_letter(18) == 's'
        assert trie.get_letter(19) == 't'
        assert trie.get_letter(20) == 'u'
        assert trie.get_letter(21) == 'v'
        assert trie.get_letter(22) == 'w'
        assert trie.get_letter(23) == 'x'
        assert trie.get_letter(24) == 'y'
        assert trie.get_letter(25) == 'z'

    # This is supposed to go through every node that it can find on the node.children list, python3 array,
    # goes in order through every node in that incidence of children possible places occupied by a node
    # This has to get in 
    # This has to do, iteratively go through every node on the index and recursively go inside to 
    # get the string starting from the last letter of the index
    def test_indexes_in_node(self):

    # This is supposed to go through every node that it can find on the node.children list, python3 array,
    # goes in order through every node in that incidence of children possible places occupied by a node
    # This has to get in 
    # This has to do, iteratively go through every node on the index and recursively go inside to 
    # get the string starting from the last letter of the index
    def test_get_string_without_prefix(self):

    # This is supposed to go through every node that it can find on the node.children list, python3 array,
    # goes in order through every node in that incidence of children possible places occupied by a node
    # This has to get in 
    # This has to do, iteratively go through every node on the index and recursively go inside to 
    # get the string starting from the last letter of the index
    def test_add_word_with_prefix_to_list(self):

    # This is supposed to go through every node that it can find on the node.children list, python3 array,
    # goes in order through every node in that incidence of children possible places occupied by a node
    # This has to get in 
    # This has to do, iteratively go through every node on the index and recursively go inside to 
    # get the string starting from the last letter of the index    
    def test_search(self):



    def test_contains_on_empty_trie(self):
        trie = Trie()
        assert trie.contains('') == True

    def test_contains_with_absent_word(self):
        trie = Trie()
        assert trie.contains('Egon') == False

    def test_single_item_trie_add_the_word_letter_by_letter_contains(self):
        # Create a trie
        trie = Trie()
        # Add a single word to it
        trie.add_the_word_letter_by_letter('egon')
        # Make sure the trie contains each word inserted
        assert trie.contains('egon') is True
        assert trie.contains('eGoN') is True
        assert trie.contains('egoN') is True
        
    def test_single_item_trie_add_the_word_letter_by_letter_contains(self):
        # Create a trie
        trie = Trie()
        # Add a single word to it
        words = ['egonn', 'yurac', 'mirva']
        for word in words:
            trie.add_the_word_letter_by_letter('egon')        
        assert trie.contains('egonn') is True
        assert trie.contains('YURAc') is True
        assert trie.contains('Mirva') is True

        assert trie.contains('egONn') is True
        assert trie.contains('Yurac') is True
        assert trie.contains('Mirva') is True

        assert trie.contains('EGoNn') is True
        assert trie.contains('yuRAC') is True
        assert trie.contains('Mirva') is True

        assert trie.contains('eGONn') is True
        assert trie.contains('yUraC') is True
        assert trie.contains('Mirva') is True

    def test_single_item_trie_add_the_word_letter_by_letter_contains(self):
        # Create a trie
        trie = Trie()
        # Add a single word to it
        words = ['eGonn', 'yUrAc', 'MirVa']
        for word in words:
            trie.add_the_word_letter_by_letter('egon')        
        assert trie.contains('egonn') is True
        assert trie.contains('yurac') is True
        assert trie.contains('mirva') is True

    def test_storage_of_words_with_almost_equal_elements(self):
        trie = Trie()
        # Add a single word to it
        words = ['eGonn', 'yUrAAc', 'MirrrVa', 
                 'eGonnn', 'yUrAc', 'MirVaaa', 
                 'eGonnnnnnn', 'yUrAaaaaaac', 'MirVa']

        for word in words:
            trie.add_the_word_letter_by_letter(word)
                
        assert trie.contains('egon') is False
        assert trie.contains('yuraaaac') is False
        assert trie.contains('mirrva') is False

        assert trie.contains('egonn') is True
        assert trie.contains('yurac') is True
        assert trie.contains('mirva') is True

        assert trie.contains('egonnnnnnnn') is False
        assert trie.contains('yuraAaaaaaac') is False
        assert trie.contains('mirvaa') is False
                
        assert trie.contains('egonnnnnn') is True
        assert trie.contains('yurac') is True
        assert trie.contains('mirva') is True

    def test_add_the_word_letter_by_letter_and_contains_on_medium_trie(self):
        # Create a trie
        trie = Trie()
        # Does it make a distinction with caps lock
        words = ['egon', 'yurac', 'mirva', 'al', 'mathew']
        for word in words:
            trie.add_the_word_letter_by_letter(word)
        # Make sure the trie contains each word inserted
        for word in words:
            assert trie.contains(word) is True
        # Make sure the trie does not contain another word
        assert trie.contains('word not in list') is False
        assert trie.contains('juan') is False
    # test that you can't add duplicate
    # test you can add words with capslock

    def test_add_the_word_letter_by_letter_and_contains_with_capital_letter(self):
                # Create a trie
        trie = Trie()
        # Does it make a distinction with caps lock
        words = ['eGon', 'yurAc', 'mIrva', 'al', 'matThEw', 'DafF']
        for word in words:
            trie.add_the_word_letter_by_letter(word)
        # Make sure the trie contains each word inserted
        for word in words:
            assert trie.contains(word) is True
        # Make sure the trie does not contain another word
        assert trie.contains('word not in list') is False
        assert trie.contains('egon') is True
        assert trie.contains('EgOn') is True
        assert trie.contains('juan') is False

if __name__ == '__main__':
    unittest.main()
