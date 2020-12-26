import sys
import unittest
from io import StringIO

# Local imports
from pile import Pile

# Globals
MAX_SIZE = sys.maxsize
ERROR = sys.stderr

"""=================================================================================
Deck Class
=================================================================================""" 

""" Deck Class
A class representing a real life deck of cards. For the context of games it can 
	represent multiple real life decks stacked together. It implements the Pile
	class and adds a few additional methods.

@author Chris P.
@created 2020-12-24 YMD
"""
class Deck(Pile):

	def __init__(self, max_size=MAX_SIZE, enforce_order=False):
		super().__init__(max_size)


# nums = []
# for i in range(0,52):
# 	nums.append(i)

# deck = Deck.fromList(nums)

# print(deck)

# print(len(deck))