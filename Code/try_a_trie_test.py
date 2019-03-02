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

    def test_contains_on_empty_trie(self):
        trie = Trie()
        assert trie.contains('Egon') == False

    def test_single_item_trie_add_the_word_letter_by_letter_contains(self):
        # Create a trie
        trie = Trie()
        # Add a single word to it
        trie.add_the_word_letter_by_letter('egon')
        # Make sure the trie contains each word inserted
        assert trie.contains('egon') is True
        assert trie.contains('') is True
        assert trie.contains('Egonn') is False
        assert trie.contains('Yurac') is False
        assert trie.contains('Mirva') is False

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

    # 

if __name__ == '__main__':
    unittest.main()
