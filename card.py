import math

""" id to (value,suit) mapping

id = (value - 2) + (suit * 13)

...

value = (id % 13) + 2
suit = floor(id / 13)
"""

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
			value = 0
		# Out of bounds will set suit to zero
		if suit < 0 or suit > 3:
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
			id_ = 0
		return cls(((id_ % 13) + 2),math.floor(id_ / 13))

	""" getValue
	Gets the value of the card
	@return int value of the card in range [2,14]
	"""
	def getValue(self):
		return self.value

	"""	getSuit
	Gets the suit of the card
	@return int suit of the card in range [0,3]
	"""
	def getSuit(self):
		return self.suit

	"""	getID
	Gets the ID of the card
	@return int ID of the card in range [0,51]
	"""
	def getID(self):
		return ((self.value - 2) + (self.suit * 13))


	# Override string - convert the value and suit to a string
	# @return 	string in format "{value} of {suit}"
	# @source
	# 	https://www.geeksforgeeks.org/switch-case-in-python-replacement/
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

	# Override representation - convert the value and suit to a string
	# @return 	string in format "{value} of {suit}"
	def __repr__(self):
		return self.__str__()