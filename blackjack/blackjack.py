# Arjun Sabnis
# blackjack.py - Implementation of Blackjack game logic

from hand import Hand
from card import Card

class Blackjack(object):
    
    def __init__(self, money):
        self.player_money = money
        self.player_bet = 0
        self.player_hand = Hand("Player")
        self.dealer_hand = Hand("Dealer")
        self.player_choice = "None"

    # Query player choice until player chooses either hit or stand    
    def query_player(self):
        decision = raw_input("What would you like to do? Enter (h)it or (s)tand: ")
        
        while (decision != "s" and decision != "h"):
            decision = raw_input("What would you like to do? Enter (h)it or (s)tand: ")

        if (decision == "h"):
            self.player_choice = "HIT"
        else:
            self.player_choice = "STAND"

        return self.player_choice

    # Ask player if they want to double down on their hand
    def double_down(self):
        down = raw_input("Would you like to double down? Enter (y)es or (n)o: ")

        while (down != "y" and down != "n"):
            down = raw_input("Would you like to double down? Enter (y)es or (n)o: ")
        
        # If selected, player gets additional card, doubles bet, and stands
        if (down == "y"):
            self.player_bet = self.player_bet * 2
            self.player_hand.add_card()
            self.player_hand.print_hand()
            self.player_choice = "STAND"

        if (down == "n"):
            self.player_choice = self.query_player()

    # Implements game logic 
    def play(self, bet):
        # Set initial bet
        self.player_bet = bet
        
        # Deal dealer's hand
        self.dealer_hand.add_card()
        self.dealer_hand.add_card()
        self.dealer_hand.print_first_card()

        # Deal player's hand
        self.player_hand.add_card()
        self.player_hand.add_card()
        self.player_hand.print_hand()

        # If player has Blackjack
        if (self.player_hand == 21):
            
            # If dealer has Blackjack
            if (self.dealer_hand == 21):
                self.dealer_hand.print_hand()
                print "\nTie!\nPlayer has %d dollars." % self.player_money
                return self.player_money
            
            # If only player has Blackjack
            elif (self.dealer_hand < self.player_hand):
                self.player_money = self.player_monet + self.player_bet
                self.dealer_hand.print_hand()
                print "\nPlayer wins!\nPlayer has %d dollars." % self.player_money
                return self.player_money
        
        # After first hand is played, ask player for double down
        self.double_down()

        # If player is bust after double down
        if (self.player_hand > 21):
                self.player_money = self.player_money - self.player_bet
                
                if (self.player_money < 0):
                    self.player_money = 0
                
                print "\nPlayer's hand is bust.\nPlayer has %d dollars." % self.player_money
                return self.player_money
        
        # If player chooses otherwise and chooses to hit
        while (self.player_choice == "HIT"):
            self.player_hand.add_card()
            self.player_hand.print_hand()

            # If player goes bust
            if (self.player_hand > 21):
                self.player_money = self.player_money - self.player_bet
                
                if (self.player_money < 0):
                    self.player_money = 0
                
                print "\nPlayer's hand is bust.\nPlayer has %d dollars." % self.player_money
                return self.player_money

            # If player has Blackjack
            if (self.player_hand == 21):
                break

            self.query_player()

        # Once player chooses to stand, dealer will hit, then hands will be compared
        if (self.dealer_hand > 17):
            self.dealer_hand.print_hand()

        # Dealer begins to hit if hand is < 17
        while (self.dealer_hand < 17):
            self.dealer_hand.add_card()
            self.dealer_hand.print_hand()

        # If dealer goes bust
        if (self.dealer_hand > 21):
            self.player_money = self.player_money + self.player_bet
            print "\nDealer's hand is bust. Player wins!\nPlayer has %d dollars." % self.player_money 
            return self.player_money

        # If dealer wins
        elif (self.dealer_hand > self.player_hand):
            self.player_money = self.player_money - self.player_bet
                
            if (self.player_money < 0):
                 self.player_money = 0

            self.dealer_hand.print_hand()    
            print "\nDealer wins.\nPlayer has %d dollars." % self.player_money
            return self.player_money

        # If player wins
        elif (self.dealer_hand < self.player_hand):
            self.player_money = self.player_money + self.player_bet
            print "\nPlayer wins!\nPlayer has %d dollars." % self.player_money 
            return self.player_money

        # If it is a tie
        elif (self.dealer_hand == self.player_hand):
            print "\nTie!\nPlayer has %d dollars." % self.player_money 
            return self.player_money
