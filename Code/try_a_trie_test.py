#!python

from try_a_trie import Node, Trie
import random
import unittest

# class Node(object):
#   def __init__(self):
# class Trie(object):
#   def __init__(self):
#   def get_node():
#   def add_word(self, word):
#   def contains(self, word):


class TrieTest(unittest.TestCase):

    def test_contains_on_empty_trie(self):
        trie = Trie()
        assert trie.contains('Egon') == False

    def test_single_item_trie_add_word_contains(self):
        # Create a trie
        trie = Trie()
        # Add a single word to it
        trie.add_word('egon')
        # Make sure the trie contains each word inserted
        assert trie.contains('egon') is True
        assert trie.contains('') is True
        assert trie.contains('Egonn') is False
        assert trie.contains('Yurac') is False
        assert trie.contains('Mirva') is False

    def test_add_word_and_contains_on_medium_trie(self):
        # Create a trie
        trie = Trie()
        # Does it make a distinction with caps lock
        words = ['egon', 'yurac', 'mirva', 'al', 'mathew']
        for word in words:
            trie.add_word(word)
        # Make sure the trie contains each word inserted
        for word in words:
            assert trie.contains(word) is True
        # Make sure the trie does not contain another word
        assert trie.contains('word not in list') is False

    # test that you can't add duplicate

    # test you can add words with capslock

    # 

if __name__ == '__main__':
    unittest.main()
