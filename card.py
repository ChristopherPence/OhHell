from io import StringIO
import math
import unittest
import sys

error = sys.stderr

""" id to (value,suit) mapping

id = (value - 2) + (suit * 13)
...
value = (id % 13) + 2
suit = floor(id / 13)
"""

"""=================================================================================
Card Class
=================================================================================""" 

""" Card Class
"Immutable" class that represents a singular real world playing card
"""
class Card:
	# Default Constructor - set the value of the card given value and suit
	# @param 	value 	: int in range [2,14] stores card value [2,3, ... ,10,J,Q,K,A]
	# @param 	suit	: int in range [0,3] stores card suit [S,D,C,H]
	def __init__(self, value, suit):
		# Out of bounds will set value to zero
		if value < 2 or value > 14:
			# revisit stderr write, conflicts with unit tests
			error.write("Invalid card value {}! Continuing with card value 0.\n".format(value))
			value = 2
		# Out of bounds will set suit to zero
		if suit < 0 or suit > 3:
			error.write("Invalid card suit {}! Continuing with card suit 0.\n".format(suit))
			suit = 0

		self.value = value
		self.suit = suit

	# "Overloaded" constructor - set the values of the card given an id in range [0,51]
	# @param	id 		: int in range [0,51] which is the unique card id
	# @return 	a corresponding Card object
	# @see		card id to card (value,suit) mapping above
	@classmethod
	def fromID(cls, id_):
		# Out of bounds will set id_ to zero
		if id_ < 0 or id_ > 51:
			error.write("Invalid card ID {}! Continuing with card ID 0.\n".format(id_))
			id_ = 0
		return cls(((id_ % 13) + 2),math.floor(id_ / 13))

	""" getValue()
	Gets the value of the card
	@return int value of the card in range [2,14]
	"""
	def getValue(self):
		return self.value

	"""	getSuit()
	Gets the suit of the card
	@return int suit of the card in range [0,3]
	"""
	def getSuit(self):
		return self.suit

	"""	getID()
	Gets the ID of the card
	@return int ID of the card in range [0,51]
	"""
	def getID(self):
		return ((self.value - 2) + (self.suit * 13))

	""" __str__()
	Override string - convert the value and suit to a string
	@return 	string in format "{value} of {suit}"
	@see https://www.geeksforgeeks.org/switch-case-in-python-replacement/
	"""
	def __str__(self):
		suit_switcher = {
			0 : "Spades",
			1 : "Diamonds",
			2 : "Clubs",
			3 : "Hearts"
		}

		value_switcher = {
			2 : "2",
			3 : "3",
			4 : "4",
			5 : "5",
			6 : "6",
			7 : "7",
			8 : "8",
			9 : "9",
			10 : "10",
			11 : "Jack",
			12 : "Queen",
			13 : "King",
			14 : "Ace"
		}

		return "{} of {}".format(value_switcher.get(self.value),suit_switcher.get(self.suit))

	""" __repr__()
	Override representation - convert the value and suit to a string
	@return 	string in format "{value} of {suit}"
	"""
	def __repr__(self):
		return self.__str__()

	""" __eq__()
	Override equality - return true if the ID's of the cards are the same. NOT checking
		if the objects are the same
	@return true if self.id = other.id
	"""
	def __eq__(self, other):
		return self.getID() == other.getID()



"""=================================================================================
Card Class Unit Tests
=================================================================================""" 

class TestCardClass(unittest.TestCase):

	# Test valid ways to create a card
	def test_valid_init(self):
		a = Card(2,1)
		self.assertEqual(a.getID(),13)
		self.assertEqual(a.getValue(),2)
		self.assertEqual(a.getSuit(),1)
		self.assertEqual(a.__str__(),"2 of Diamonds")

		b = Card.fromID(13)
		self.assertEqual(a,b)
		self.assertEqual(b.getID(),13)
		self.assertEqual(b.getValue(),2)
		self.assertEqual(b.getSuit(),1)
		self.assertEqual(b.__str__(),"2 of Diamonds")

		c = Card(7,2)
		self.assertEqual(c.getID(),31)
		self.assertEqual(c.getValue(),7)
		self.assertEqual(c.getSuit(),2)
		self.assertEqual(c.__str__(),"7 of Clubs")

		d = Card.fromID(31)
		self.assertEqual(c,d)
		self.assertEqual(d.getID(),31)
		self.assertEqual(d.getValue(),7)
		self.assertEqual(d.getSuit(),2)
		self.assertEqual(d.__str__(),"7 of Clubs")

	# Test invalid creations
	def test_invalid_init(self):
		a = Card(47,2)
		self.assertEqual(a.getValue(),2)
		self.assertEqual(a.getSuit(),2)
		self.assertEqual(a.__str__(),"2 of Clubs")

		b = Card(0,2)
		self.assertEqual(b.getValue(),2)
		self.assertEqual(b.getSuit(),2)
		self.assertEqual(b.__str__(),"2 of Clubs")

		c = Card(5,-1)
		self.assertEqual(c.getValue(),5)
		self.assertEqual(c.getSuit(),0)
		self.assertEqual(c.__str__(),"5 of Spades")

		d = Card(5,4)
		self.assertEqual(d.getValue(),5)
		self.assertEqual(d.getSuit(),0)
		self.assertEqual(d.__str__(),"5 of Spades")

		e = Card.fromID(-1)
		self.assertEqual(e.getValue(),2)
		self.assertEqual(e.getSuit(),0)
		self.assertEqual(e.__str__(),"2 of Spades")

		f = Card.fromID(52)
		self.assertEqual(f.getValue(),2)
		self.assertEqual(f.getSuit(),0)
		self.assertEqual(f.__str__(),"2 of Spades")



if __name__ == '__main__':
	# Divert stderr so unittest output isn't cluttered
	error = StringIO() 
	unittest.main()