# Arjun Sabnis
# engine.py - Implements blackjack gameplay

from blackjack import Blackjack
import random
import time


# Take bet value from player
def take_bet(money):
    bet = raw_input("Enter bet in dollars, 0 or less to quit: ")
    try:
        bet = int(bet)
    except ValueError:
        print "This was not a number, please enter a bet."

    if (bet > money):
        print "You don't have that much money! Enter a lower bet."
    
    # Repeat while player's bet is greater than their money
    while (bet > money):
        bet = raw_input("Enter bet in dollars, 0 or less to quit: ")
        try:
            bet = int(bet)
        except ValueError:
            print "This was not a number, please enter a bet."
            
        if (bet > money):
            print "You don't have that much money! Enter a lower bet."

    return bet


# -----------------------------------------------------------------------------
# Main script for game
random.seed(time.time())

print """
********************************************************************************
                   __       __   __      ____  __   __                      _
 /\    ^\/^       |  ) |   |  | |   |  /   |  |  | |   |  /        /\     _( )_
/  \  |    |      |--  |   |--| |   |--    |  |--| |   |--        /  \   (     )
\  /   \  /       |__) |__ |  | |__ |  | __|  |  | |__ |  |      (_  _)   (_ _)
 \/     \/                                                         ||      /_\\
                              Go big or go home!

********************************************************************************


"""

# Player starts with 500 dollars
money = 500
round_num = 1

print "Player starts with %d dollars." % money
print """

********************************************************************************
"""
print "Round %d\n" % round_num

# Take bet from user
bet = take_bet(money)

# Keep playing the game until user is broke or bets 0
while (money > 0) and (bet > 0): 
    game = Blackjack(money)

    # Play a round
    money = game.play(bet)

    # Take a new bet unless player is broke
    if (money > 0):
        round_num = round_num + 1
        print """

********************************************************************************
        """
        print "Round %d\n" % round_num
        bet = take_bet(money)

print """
********************************************************************************
                    
                    Game over! Thank you for playing!

********************************************************************************
"""
