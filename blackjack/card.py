# Arjun Sabnis
# card.py - Implementation of cards in blackjack hand

from random import randint

# Class card to create cards in hand
class Card(object):

    # Dict for card names
    _card_names = {
            1: "Ace",
            2:  "Two",
            3:  "Three",
            4:  "Four",
            5:  "Five",
            6:  "Six",
            7:  "Seven",
            8:  "Eight",
            9:  "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
            }
    
    # Dict for card values
    _card_values = {
            1: 11,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 10,
            12: 10,
            13: 10
            }
    
    # Takes value parameter for testing purposes
    def __init__(self): 
        # Randomly select card type
        select = randint(1,13)
        self.type = self._card_names.get(select)
        self.value = self._card_values.get(select)
    
    def get_type(self):
        return self.type

    def get_value(self):
        return self.value
