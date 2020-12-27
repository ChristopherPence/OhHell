import sys
import time
import math

# Local imports
from card import Card
from pile import Pile
from deck import Deck
from player import Player
from gamestate import Gamestate

# Globals
MAX_SIZE = sys.maxsize
regular_deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]


class Game():

	def __init__(self, game_name):
		self.game_name = game_name

		# Set the parameters for each game type
		if self.game_name == "Oh Hell":
			self.min_players = 3
			self.max_players = 7
			self.num_decks = 1
			self.valid_cards = regular_deck

		elif self.game_name == "Rummy":
			self.min_players = 2
			self.max_players = 7
			self.num_decks = 1
			self.valid_cards = regular_deck

		else:
			# Set default of game parameters
			self.min_players = 4
			self.max_players = 4
			self.num_decks = 1
			self.valid_cards = regular_deck

		# Get Number of Players
		print("Starting game: {}".format(self.game_name))
		num_players = int(input("How many players are playing? "))
		while(num_players < self.min_players or num_players > self.max_players):
			num_players = int(input("{} isn't a valid number of players, please enter a new amount: ".format(num_players)))
		self.num_players = num_players

		# Enter the player names in order
		players = []
		for i in range(0, self.num_players):
			name = input("Enter the name of player {}: ".format(i+1))
			date = math.floor(time.time())
			id_ = name + "-" + str(date)
			players.append(Player(name, id_))

		# Build the deck of cards
		deck = Deck(self.num_decks * len(self.valid_cards), enforce_order=False)
		for i in range(0, self.num_decks):
			for j in self.valid_cards:
				deck.append(Card.fromID(j))

		# Create the gamestate object, likely will switch to using a factory
		# since some games will need special gamestate attributes like current suit in Oh Hell
		self.gamestate = Gamestate(deck, players)
		print(self.gamestate)

		# Start the first action
		print("Actions not implemented yet. Ending game.")