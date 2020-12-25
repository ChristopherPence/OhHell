import sys
import unittest
from io import StringIO

# Local imports
from card import *

# Globals
MAX_SIZE = sys.maxsize
ERROR = sys.stderr

"""=================================================================================
Pile Class
================================================================================="""

""" Pile Class
A class representing a real life "pile" of cards.

@author Chris P.
@created 2020-12-21 YMD
"""
class Pile():
	"""__init__
	Default Constructor - creates an empty pile object with the optional max_size parameter
	@param max_size : INT coressponding to the maximum size of the pile
	"""
	def __init__(self, max_size=MAX_SIZE):
		self.max_size = max_size
		self.cards = []

	# ------------------------------------------------------------------------------
	# Static Methods

	""" fromList(lis)
	"Overloaded" constructor - Creates a pile object containing cards with IDs corresponding to the ints in lis
	@param lis : [int] - list of card IDs
	@return a corresponding Pile object
	"""
	@classmethod
	def fromList(cls, lis, max_size=MAX_SIZE):
		output = cls(max_size)
		for i in lis:
			output.append(Card.fromID(i))
		return output

	# ------------------------------------------------------------------------------
	# Public Methods

	""" insert(card, location)
	Inserts a card at the given location. Default location is 0.
	@param card : Card - the card to insert into the deck. Cards are "immutable" and singletons so shallow copy
	@param location : INT - the location in the pile to insert the card. Default is 0
	"""
	def insert(self, card, location=0):
		return self.cards.insert(location,card)

	""" remove(card)
	Removes a specified card from the list if present. It will only remove one instance of the card. 
		Potentially unsafe if List.remove() features change...
	@param card : Card that represents the card to remove
	"""
	def remove(self, card):
		return self.cards.remove(card)

	""" push(card)
	Push a card to the front (location 0) of the list. Carried out by calling Pile.insert()
	@param card : Card - the card to push to the front. See the notes for Pile.insert()
	"""
	def push(self, card):
		return self.insert(card,0)

	""" pop()
	Pop a card from the front of the list
	@return Card that was at the front of the list
	"""
	def pop(self):
		return self.cards.pop(0)

	""" append(card)
	Append a card to the end of the list
	@param card : Card - The card to append to the end of the list. See the notes for Pile.insert() about copies
	"""
	def append(self, card):
		return self.cards.append(card)

	""" sort()
	Numerically sorts the contents of self.cards
	"""
	def sort(self):
		self.cards.sort()

	""" clear()
	Removes all of contents from self.hand
	"""
	def clear(self):
		self.cards.clear()

	""" getSize()
	Returns the size of hand list in a Pile object
	@return length of self.hand
	"""
	def getSize(self):
		return len(self.cards)

	# ------------------------------------------------------------------------------
	# Python Methods

	""" __len__()
	Overrides the __len__ method and returns the size of hand list in a Pile object
	@return length of self.hand
	"""
	def __len__(self):
		return self.getSize()

	""" __str__()
	Overrides the __str__ method and returns a string 
	@return string representation of self.hand
	"""
	def __str__(self):
		return self.cards.__str__()

	""" __repr__()
	Overrides the __repr__ method and returns a string 
	@return string representation of self.hand
	"""
	def __repr__(self):
		return self.__str__()