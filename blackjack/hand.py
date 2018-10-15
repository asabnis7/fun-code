# Arjun Sabnis
# hand.py - Implementation of Blackjack hand

from card import Card

class Hand(object):

    def __init__(self, person):
        self.hand_holder = person   # Holds either Player or Dealer
        self.value = 0              # Value of player's hand
        self.num_aces = 0           # Number of aces in hand - useful for value
        self.num_cards = 0          # Number of cards in hand
        self.cards = []             # Actual cards in player's hand

    # Print player's hand
    def print_hand(self):
        print "\n%s's hand is: " % self.hand_holder,

        for i in range(self.num_cards):
            print "%s " % self.cards[i].get_type(),

        print "\n%s's hand value is: %d" % (self.hand_holder, self.value)

    # Print dealer's first card
    def print_first_card(self):
        print "\nDealer's first card is: %s" % self.cards[0].get_type()

    # Update hand's value after inserting new card
    def _update_value(self):
        self.num_aces = 0;
        total = 0

        for i in range(self.num_cards):
            total = total + self.cards[i].get_value()
            card_name = self.cards[i].get_type()

            if (card_name == "Ace"):
                self.num_aces = self.num_aces + 1
            
            # Change value of ace from 11 to 1 if hand value exceeds 21
            while (total > 21 and self.num_aces > 0):
                total = total - 10
                self.num_aces = self.num_aces - 1

        self.value = total

    # Add random card to player hand
    def add_card(self):
        self.cards.append(Card())
        self.num_cards = self.num_cards + 1
        self._update_value()

    # Overload greater than to compare hands
    def __gt__(self, other_hand):
        return self.value > other_hand.value

    # Overload greater than to compare hand with a given value
    def __gt__(self, value):
        return self.value > value

    # Overload less than to compare hands
    def __lt__(self, other_hand):
        return self.value < other_hand.value

    # Overload less than to compare hand with a given value
    def __lt__(self, value):
        return self.value < value

    # Overload equals to compare hands
    def __eq__(self, other_hand):
        return self.value ==  other_hand.value

    # Overload equals to compare hand with given value
    def __eq__(self, value):
        return self.value == value
