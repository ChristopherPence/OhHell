import sys
import unittest
from io import StringIO
import random

# Local imports
from deck import *

# Globals
MAX_SIZE = sys.maxsize
ERROR = sys.stderr

"""=================================================================================
DeckSimulation Class
=================================================================================""" 

"""
hi

"""
class DeckSimulation(Deck):

	def __init__(self, max_size=MAX_SIZE):
		super().__init__(max_size)

	""" shuffle()
	Randomly orders the contents of self.hand 
	"""
	def shuffle(self):
		random.shuffle(self.cards)


deck = DeckSimulation(52)
deck.push(Card(3,3))
deck.push(Card(4,3))
deck.push(Card(12,1))

print(deck)

deck.sort()

print(deck)

deck.shuffle()

print(deck)
