import sys
import unittest
import random
from io import StringIO

# Local imports
from card import Card
from error import *

# Globals
MAX_SIZE = sys.maxsize

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
	def __init__(self, max_size=MAX_SIZE, enforce_order=False):
		self.enforce_order = enforce_order
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
	@returns true if successful, false if failed
	"""
	def insert(self, card, location=0):
		if self.getSize() < self.max_size:
			self.cards.insert(location,card)
			return True #Isn't certain to be a successful insert, but list.insert returns nothing...
		else:
			ERROR.write("Invalid Insert: Inserting into pile would violate max_size.")
			return False

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
		if self.getSize() < self.max_size:
			self.cards.append(card)
			return True
		else:
			ERROR.write("Invalid Append: Inserting into pile would violate max_size.")
			return False

	""" sort()
	Numerically sorts the contents of self.cards if self.enforce_order == False
	"""
	def sort(self):
		if self.enforce_order == False:
			self.cards.sort()
		else:
			ERROR.write("WARNING: Trying to sort pile with an enforced order. Not sorting.")

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

	""" __contains__(other)
	Checks if other (a card Object...) is contained within the pile
	@pre type(other) == Card
	@param other : Card - the card to check the presence of.
	"""
	def __contains__(self, other):
		if type(other) != type(Card(2,0)): # Confirm types are the same
			return False
		elif other in self.cards: #Check if the card is contained
			return True
		else:
			return False



"""=================================================================================
Pile Class Unit Tests
=================================================================================""" 

class TestPileClass(unittest.TestCase):
	def setUp(self):
		self.poker1 = Pile(2)
		self.poker2 = Pile(2)
		self.rumy_table  = Pile(enforce_order=True)
		self.rumy1 = Pile()
		self.rumy2 = Pile()

	def test_inserts(self):
		# Test calling insert 3 times on max_size=2
		self.assertTrue(self.poker1.insert(Card.fromID(47)))
		self.assertTrue(self.poker1.insert(Card.fromID(33)))
		self.assertFalse(self.poker1.insert(Card.fromID(21)))
		self.assertEqual(self.poker1.__str__(),"[9 of Clubs, 10 of Hearts]")

		# Test calling append
		self.assertFalse(self.poker1.append(Card.fromID(21)))
		self.assertEqual(self.poker1.__str__(),"[9 of Clubs, 10 of Hearts]")

	def test_enforce_order(self):
		# Simulate a multiple turns of Rumy's table pile
		self.rumy_table.push(Card.fromID(33))
		self.rumy_table.push(Card.fromID(47))
		self.rumy_table.push(Card.fromID(21))

		# Assert nothing changes after a sort
		self.assertEqual(self.rumy_table.__str__(), "[10 of Diamonds, 10 of Hearts, 9 of Clubs]")
		self.rumy_table.sort()
		self.assertEqual(self.rumy_table.__str__(), "[10 of Diamonds, 10 of Hearts, 9 of Clubs]")
		# self.assertEqual(self.rumy_table.__str__(), "[10 of Diamonds, 9 of Clubs, 10 of Hearts]")

	# Test the __contains__ python method
	def test_pile_contains(self):
		self.rumy1.push(Card.fromID(33))
		self.rumy1.push(Card.fromID(47))
		self.rumy1.push(Card.fromID(21))

		# Test the same card, different object
		self.assertTrue(Card.fromID(47) in self.rumy1)
		self.assertTrue(Card(10,3) in self.rumy1) 

		self.assertFalse(Card.fromID(48) in self.rumy1)
		self.assertFalse(Card(10,2) in self.rumy1)
		self.assertFalse(Card(11,3) in self.rumy1)
		self.assertFalse("Hello World" in self.rumy1)
		self.assertFalse(7 in self.rumy1)

	# Test sorting a hand of 3 cards
	def test_sort_easy(self):
		self.rumy1.push(Card.fromID(33))
		self.rumy1.push(Card.fromID(47))
		self.rumy1.push(Card.fromID(21))

		self.assertEqual(self.rumy1.__str__(), "[10 of Diamonds, 10 of Hearts, 9 of Clubs]")
		self.rumy1.sort()
		self.assertEqual(self.rumy1.__str__(), "[10 of Diamonds, 9 of Clubs, 10 of Hearts]")

	# Test sorting two decks of randomly ordered cards
	def test_sort_hard(self):
		# Get the randomly sorted numbers
		nums = []
		for j in range(0,2):
			for i in range(0,52):
				nums.append(i)
		random.shuffle(nums)
		self.assertTrue(len(nums) == 104)

		# Turn the list of numbers into a deck and sort the cards
		deck = Pile.fromList(nums)
		self.assertTrue(deck.getSize() == 104)
		deck.sort()
		self.assertEqual(deck.__str__(),"""[2 of Spades, 2 of Spades, 3 of Spades, 3 of Spades, 4 of Spades, 4 of Spades, 5 of Spades, 5 of Spades, 6 of Spades, 6 of Spades, 7 of Spades, 7 of Spades, 8 of Spades, 8 of Spades, 9 of Spades, 9 of Spades, 10 of Spades, 10 of Spades, Jack of Spades, Jack of Spades, Queen of Spades, Queen of Spades, King of Spades, King of Spades, Ace of Spades, Ace of Spades, 2 of Diamonds, 2 of Diamonds, 3 of Diamonds, 3 of Diamonds, 4 of Diamonds, 4 of Diamonds, 5 of Diamonds, 5 of Diamonds, 6 of Diamonds, 6 of Diamonds, 7 of Diamonds, 7 of Diamonds, 8 of Diamonds, 8 of Diamonds, 9 of Diamonds, 9 of Diamonds, 10 of Diamonds, 10 of Diamonds, Jack of Diamonds, Jack of Diamonds, Queen of Diamonds, Queen of Diamonds, King of Diamonds, King of Diamonds, Ace of Diamonds, Ace of Diamonds, 2 of Clubs, 2 of Clubs, 3 of Clubs, 3 of Clubs, 4 of Clubs, 4 of Clubs, 5 of Clubs, 5 of Clubs, 6 of Clubs, 6 of Clubs, 7 of Clubs, 7 of Clubs, 8 of Clubs, 8 of Clubs, 9 of Clubs, 9 of Clubs, 10 of Clubs, 10 of Clubs, Jack of Clubs, Jack of Clubs, Queen of Clubs, Queen of Clubs, King of Clubs, King of Clubs, Ace of Clubs, Ace of Clubs, 2 of Hearts, 2 of Hearts, 3 of Hearts, 3 of Hearts, 4 of Hearts, 4 of Hearts, 5 of Hearts, 5 of Hearts, 6 of Hearts, 6 of Hearts, 7 of Hearts, 7 of Hearts, 8 of Hearts, 8 of Hearts, 9 of Hearts, 9 of Hearts, 10 of Hearts, 10 of Hearts, Jack of Hearts, Jack of Hearts, Queen of Hearts, Queen of Hearts, King of Hearts, King of Hearts, Ace of Hearts, Ace of Hearts]""")

	def tearDown(self):
		self.poker1.clear()
		self.poker2.clear()
		self.rumy_table.clear()
		self.rumy1.clear()
		self.rumy2.clear()



if __name__ == '__main__':
	# Divert stderr so unittest output isn't cluttered
	ERROR = StringIO() 
	unittest.main()