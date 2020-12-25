default: pile

dev: 
	python3 src/pile.py

# pile.py unittests
pile: 
	python3 src/pile.py

# card.py unittests
card: 
	python3 src/card.py

deck:
	python3 src/deck.py

deck_simulation:
	python3 src/deck_simulation.py
