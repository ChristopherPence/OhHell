import sys
import unittest
from io import StringIO

# Local imports
from card import Card
from pile import Pile
from player import Player
from error import *

# Globals
MAX_SIZE = sys.maxsize

"""=================================================================================
Gamestate Class
================================================================================="""

""" Gamestate Class
The definitive source of truth for a given game. Stores all the information related
	to the game being played like players and what cards are where. It also stores
	the history of actions taken to get to that point in time.

@author Chris P.
@created 2020-12-26 YMD
"""
class Gamestate():

	""" __init__
	Default constructor - creates a gamestate object with given deck and player array. 
		Also create the empty array of piles. 
	@param deck : Deck - the full deck of cards to start the game with.
	@param players[] : Array of Player objects. These are the players in the current game
	"""
	def __init__(self, deck, players):
		self.deck = deck
		self.players = players
		self.piles = []



