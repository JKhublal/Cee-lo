from random import randint
#from time import #sleep
print '***********CEE-LO***********'
print '--------Alpha Version-------'
print '-by Psydungeon Laboratories-'
print

# Define a function that displays the rules.
def print_rules():
    print "-" * 20
    print "Cee-lo is a dice game that originated in China and is played around the world."
    print "Here's a great article about Cee-lo in the United States: http://www.nytimes.com/2009/08/16/nyregion/16ritual.html?_r=1&"
    print "This version of Cee-lo uses the same rules found in Sega's 'RYU GA GOTOKU/YAKUZA' series."
    print "-" * 20
    print "=====PLAYERS====="
    print "There are four players: The banker, and three individual players." 
    print "In every game of Cee-lo, each player will take a turn as the banker."
    print "The banker rolls first, and the other players try to beat the banker's hand. The other players compete only with the banker, not with each other."
    print "The banker has a slightly higher chance of winning, but they also stand to lose a lot of money."
    print raw_input("Press enter to learn about ROUNDS.")
    print "=====ROUNDS====="
    print "Each player rolls three dice. They get 3 chances to roll a scoring HAND."
    print "If a player doesn't roll a scoring hand after 3 tries, they lose that ROUND."
    print "The banker rolls first. Depending on their HAND, they can instantly win or lose the ROUND. More on this later."
    print "After 4 ROUNDS, you will have the option to continue playing or quit."
    print raw_input("Press enter to learn about HANDS.")     
    print "=====HANDS====="
    print
    print "***POINT"
    print "Roll a double of any number, and the third die is the POINT."
    print "For example, if you roll 4 - 4 - 6, your point is 6."
    print "The higher point wins. For example, if the banker's point is 5 and the player's point is 2, the banker wins."
    print "A point of 1 is an instant loss."
    print
    print "***4 - 5 - 6"
    print "If a player rolls 4 - 5 - 6 in any order, they instantly win. If the banker rolls 4 - 5 - 6, everyone else loses."
    print
    print "***Trips"
    print "If a player rolls three of the same number (for example, 4 - 4 - 4), they instantly win."
    print "If the banker rolls TRIPS, everyone else instantly loses."
    print
    print "***1 - 2 - 3"
    print "If a player rolls 1 - 2 - 3 in any order, they instantly lose. If the banker rolls 1 - 2 - 3, everyone else wins."
    print 
    print "***No Score"
    print "If a player doesn't roll a scoring hand after three tries, they lose."
    print "If the banker doesn't roll a scoring hand after three tries, everyone else wins."
    print
    print "***Banker Instant Win Conditions:"
    print "Trips, 4 - 5 - 6, point 6"
    print
    print "***Banker Instant Lose Conditions:"
    print "1 - 2 - 3, point 1, no score after three tries"


# Define parent class where Player Data is stored.
class Player_data(object):

    human = True 
    def __init__(self, name):
        self.name = name
        self.wallet = 500
        self.order = 0
        self.is_banker = False
        self.point = 0
        self.bet = 0

    # Define a function for the player to place a bet. This will be automated for COM opponents.   
    def place_bet(self): 
        print "You have %s coins." % self.wallet
        self.bet = int(raw_input("How much do you want to bet?: "))    
        # Make sure they aren't betting more than they have.
        while self.bet > self.wallet:
            print "You don't have that many coins. Your bet needs to be %s coins or less." % (player.wallet)
            print
            self.bet = int(raw_input("How much do you want to bet?: "))
            
         
    def roll_dice(self):
        turns_left = 3
        print raw_input("Your turn. Press enter to roll the dice. ")
        while turns_left > 0:
            # Roll three dice
            self.roll_1 = randint(1, 3)
            self.roll_2 = randint(1, 3)
            self.roll_3 = randint(1, 3)
            turns_left -= 1
            print "You rolled %s" % (self.roll_1),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s" % (self.roll_2),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s." % (self.roll_3)
            #sleep(0.5)
            
            # If a triple is rolled...
            if self.roll_1 == self.roll_2 and self.roll_1 == self.roll_3:
                self.point = "trips"
                print "TRIPS! You rolled a triple %s." % (self.roll_1)
                break
            # If 4-5-6 is rolled...
            elif (self.roll_1 == 4 and self.roll_2 == 5 and self.roll_3 == 6) or (self.roll_1 == 5 and self.roll_2 == 6 and self.roll_3 == 4) or (self.roll_1 == 6 and self.roll_2 == 4 and self.roll_3 == 5) or (self.roll_1 == 4 and self.roll_2 == 6 and self.roll_3 == 5) or (self.roll_1 == 5 and self.roll_2 == 4 and self.roll_3 == 6) or (self.roll_1 == 6 and self.roll_2 == 5 and self.roll_3 == 4):
                self.point = 456
                print "BOOM! You rolled 4-5-6!"
                break
            # If 1-2-3 is rolled...
            elif (self.roll_1 == 1 and self.roll_2 == 2 and self.roll_3 == 3) or (self.roll_1 == 2 and self.roll_2 == 3 and self.roll_3 == 1) or (self.roll_1 == 3 and self.roll_2 == 2 and self.roll_3 == 1) or (self.roll_1 == 1 and self.roll_2 == 3 and self.roll_3 == 2) or (self.roll_1 == 2 and self.roll_2 == 1 and self.roll_3 == 3) or (self.roll_1 == 3 and self.roll_2 == 1 and self.roll_3 == 2): 
                self.point = 123
                print "Weak! You rolled 1-2-3!"
                break
            # If no point is rolled...
            elif self.roll_1 != self.roll_2 and self.roll_1 != self.roll_3 and self.roll_2 != self.roll_3:
                if turns_left > 0:
                    self.point = 0
                    print raw_input("No score. Press enter to roll again. ")
            # If roll 1 and roll 2 are the same, set roll 3 as player's point.        
            elif self.roll_1 == self.roll_2:
                self.point = self.roll_3
                if self.roll_3 == 1:
                    # If their point is 1, they lose.
                    print "Bummer! Your point is 1." 
                    break
                else:
                    print "Your point is %s." % (self.point)
                    #print "\n"
                    break
            # If roll 2 and roll 3 are the same number, set roll 1 as player's point.    
            elif self.roll_2 == self.roll_3:
                self.point = self.roll_1
                if self.roll_1 == 1:
                    print "Bummer! Your point is 1" 
                    #print "\n"
                    break
                else:
                    print "Your point is %s." % (self.point)
                    #print "\n"
                    break
            # If roll 1 and roll 3 are the same number, set roll 2 as player's point.    
            elif self.roll_1 == self.roll_3:
                self.point = self.roll_2
                if self.roll_2 == 1:
                    print "Bummer! Your point is 1." 
                    break
                else:
                    print "Your point is %s." % (self.point)
                    #print "\n"
                    #print raw_input("Press enter to continue. ")
                    break                         
        else:
            print "Dammit Beavis, you didn't score."

    def banker_roll_dice(self): # Roll dice function for the banker.
        turns_left = 3
        banker_point = 0
        print raw_input("Banker's turn. Press enter to roll the dice. ")
        while turns_left > 0:
            # Roll three dice
            self.roll_1 = randint(1, 6)
            self.roll_2 = randint(1, 6)
            self.roll_3 = randint(1, 6)
            turns_left -= 1
            print "%s rolled %s" % (self.name, self.roll_1),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s" % (self.roll_2),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s." % (self.roll_3)
            #sleep(0.5)
            #remove print "%s rolled %s - %s - %s." % (self.name, self.roll_1, self.roll_2, self.roll_3)
            
            # If a triple is rolled...
            if self.roll_1 == self.roll_2 and self.roll_1 == self.roll_3:
                self.point = "trips"
                print "TRIPS! %s rolled a triple %s. The banker wins this round." % (self.name, self.roll_1)
                break
            # If 4-5-6 is rolled...
            elif (self.roll_1 == 4 and self.roll_2 == 5 and self.roll_3 == 6) or (self.roll_1 == 5 and self.roll_2 == 6 and self.roll_3 == 4) or (self.roll_1 == 6 and self.roll_2 == 4 and self.roll_3 == 5) or (self.roll_1 == 4 and self.roll_2 == 6 and self.roll_3 == 5) or (self.roll_1 == 5 and self.roll_2 == 4 and self.roll_3 == 6) or (self.roll_1 == 6 and self.roll_2 == 5 and self.roll_3 == 4):
                self.point = 456
                print "BOOM! %s rolled 4-5-6! The banker wins this round." % (self.name)
                break
            # If 1-2-3 is rolled...
            elif (self.roll_1 == 1 and self.roll_2 == 2 and self.roll_3 == 3) or (self.roll_1 == 2 and self.roll_2 == 3 and self.roll_3 == 1) or (self.roll_1 == 3 and self.roll_2 == 2 and self.roll_3 == 1) or (self.roll_1 == 1 and self.roll_2 == 3 and self.roll_3 == 2) or (self.roll_1 == 2 and self.roll_2 == 1 and self.roll_3 == 3) or (self.roll_1 == 3 and self.roll_2 == 1 and self.roll_3 == 2): 
                self.point = 123
                print "Yikes! %s rolled 1-2-3! The banker loses this round. Everyone else wins!" % (self.name)
                break
            # If no point is rolled...
            elif self.roll_1 != self.roll_2 and self.roll_1 != self.roll_3 and self.roll_2 != self.roll_3:
                if turns_left > 0:
                    print raw_input("No score. Press enter. ")            
            # If no point is rolled...
            elif self.roll_1 != self.roll_2 and self.roll_1 != self.roll_3 and self.roll_2 != self.roll_3:
                if turns_left > 0:
                    print raw_input("No score. Press enter. ")
            # If roll 1 and roll 2 are the same, set roll 3 as player's point.        
            elif self.roll_1 == self.roll_2:
                self.point = self.roll_3
                if self.roll_3 == 1:
                    # If their point is 1, they lose.
                    print "%s's point is 1. The banker loses this round. Everyone else wins!" % (self.name)                   
                    break
                else:
                    print "Banker's point is %s." % (self.point)
                    print
                    break
            # If roll 2 and roll 3 are the same number, set roll 1 as player's point.    
            elif self.roll_2 == self.roll_3:
                self.point = self.roll_1
                if self.roll_1 == 1:                    
                    print "%s's point is 1. The banker loses this round. Everyone else wins!" % (self.name) 
                    break
                else:
                    print "Banker's point is %s." % (self.point)
                    print
                    break
            # If roll 1 and roll 3 are the same number, set roll 2 as player's point.    
            elif self.roll_1 == self.roll_3:
                self.point = self.roll_2
                if self.roll_2 == 1:
                    print "%s's point is 1. The banker loses this round. Everyone else wins!" % (self.name) 
                    break
                else:
                    print "Banker's point is %s." % (self.point)
                    print
                    break
                    #print raw_input("Press enter to continue. ") --- maybe this isn't necessary
                    break                         
        else:
            print "Too bad, %s didn't score. Everyone else wins!" % (self.name) 

# Define subclass for computer opponents.
class COM_data(Player_data):

    human = False
    def __init__(self, name):
        self.name = name
        self.wallet = randint(420, 700)
        self.order = 0
        self.is_banker = False
        self.point = 0
        self.bet = 0

    # Define a function for the COM to place a bet automatically. COM should not be able to run out of money.   
    def place_bet(self): 
        print "%s has %s coins." % (self.name,self.wallet)
        self.bet = randint(self.wallet/4,self.wallet/3)
        print "%s bets %s coins." % (self.name,self.bet)
    def roll_dice(self): # COM roll dice function. Same as for player but uses COM's name instead of 'you'
        turns_left = 3
        print raw_input(self.name + "'s turn. Press enter to roll the dice. ") #% (self.name)
        while turns_left > 0:
            # Roll three dice
            self.roll_1 = randint(1, 6)
            self.roll_2 = randint(1, 6)
            self.roll_3 = randint(1, 6)
            turns_left -= 1
            print "%s rolled %s" % (self.name, self.roll_1),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s" % (self.roll_2),
            #sleep(0.25)
            print "-",
            #sleep(0.25)
            print "%s." % (self.roll_3)
            #sleep(0.5)
            #remove print "%s rolled %s - %s - %s." % (self.name, self.roll_1, self.roll_2, self.roll_3)

            # If a triple is rolled...
            if self.roll_1 == self.roll_2 and self.roll_1 == self.roll_3:
                self.point = "trips"
                print "TRIPS! %s rolled a triple %s." % (self.name, self.roll_1)
                break
            # If 4-5-6 is rolled...
            elif (self.roll_1 == 4 and self.roll_2 == 5 and self.roll_3 == 6) or (self.roll_1 == 5 and self.roll_2 == 6 and self.roll_3 == 4) or (self.roll_1 == 6 and self.roll_2 == 4 and self.roll_3 == 5) or (self.roll_1 == 4 and self.roll_2 == 6 and self.roll_3 == 5) or (self.roll_1 == 5 and self.roll_2 == 4 and self.roll_3 == 6) or (self.roll_1 == 6 and self.roll_2 == 5 and self.roll_3 == 4):
                self.point = 456
                print "BOOM! %s rolled 4-5-6!" % (self.name)
                break
            # If 1-2-3 is rolled...
            elif (self.roll_1 == 1 and self.roll_2 == 2 and self.roll_3 == 3) or (self.roll_1 == 2 and self.roll_2 == 3 and self.roll_3 == 1) or (self.roll_1 == 3 and self.roll_2 == 2 and self.roll_3 == 1) or (self.roll_1 == 1 and self.roll_2 == 3 and self.roll_3 == 2) or (self.roll_1 == 2 and self.roll_2 == 1 and self.roll_3 == 3) or (self.roll_1 == 3 and self.roll_2 == 1 and self.roll_3 == 2): 
                self.point = 123
                print "Weak! %s rolled 1-2-3!" % (self.name)
                break
            # If no point is rolled...
            elif self.roll_1 != self.roll_2 and self.roll_1 != self.roll_3 and self.roll_2 != self.roll_3:
                if turns_left > 0:
                    print raw_input("No score. Press enter. ")
            # If roll 1 and roll 2 are the same, set roll 3 as player's point.        
            elif self.roll_1 == self.roll_2:
                self.point = self.roll_3
                if self.roll_3 == 1:
                    # If their point is 1, they lose.
                    print "Bummer! %s's point is 1." % (self.name)
                    break
                else:
                    print "%s's point is %s." % (self.name, self.point)
                    break
            # If roll 2 and roll 3 are the same number, set roll 1 as player's point.    
            elif self.roll_2 == self.roll_3:
                self.point = self.roll_1
                if self.roll_1 == 1:                    
                    print "Bummer! %s's point is 1." % (self.name)
                    break
                else:
                    print "%s's point is %s." % (self.name, self.point)
                    break
            # If roll 1 and roll 3 are the same number, set roll 2 as player's point.    
            elif self.roll_1 == self.roll_3:
                self.point = self.roll_2
                if self.roll_2 == 1:
                    print "Bummer! %s's point is 1." % (self.name)
                    break
                else:
                    print "%s's point is %s." % (self.name, self.point)
                    # print
                    break
                    #print raw_input("Press enter to continue. ") --- maybe this isn't necessary
                    break                         
        else:
            print "Too bad, %s didn't score." % (self.name)
           
                          
    
# Define a list of possible opponents to pull from at random
COM_names = ["Poos", "Chichin", "Jimpoos", "Manatee", "Kumo", "Discopoos", "Esapoos", "Barack Obama", "Kim Jong Un", "Vladimir Putin", "Your Mom", "A Herd of Highly-Sentient Goats", "Oprah"]

# Choose three opponents at random from the list. After a name is selected, it is removed from the list.
com_1 = COM_data(COM_names[randint(0,len(COM_names)-1)])
COM_names.remove(com_1.name)

com_2 = COM_data(COM_names[randint(0,len(COM_names)-1)])
COM_names.remove(com_2.name)

com_3 = COM_data(COM_names[randint(0,len(COM_names)-1)])
COM_names.remove(com_3.name)
  
# Let's get to know each other.        

player = Player_data(raw_input("What is your name?: "))
know_rules = raw_input("Do you know the rules of Cee-lo? Enter Y or N: ").lower()
while know_rules != 'y' and know_rules != 'n':
    know_rules = raw_input("OOPS! That was neither a Y nor an N. Try again: ")
    print
else:
    while know_rules == 'n':
        print_rules()
        print
        know_rules = raw_input("Got it now? Enter Y or N: ").lower()
        while know_rules != 'y' and know_rules != 'n':
            know_rules = raw_input("OOPS! That was neither a Y nor an N. Try again: ")
            print
        
    else:
        print "Great! Let's play Cee-lo. I'll give you 500 coins to bet." + "\n"

    print "Your opponents are %s, %s, and %s." % (com_1.name, com_2.name, com_3.name)    
    print

all_players = [player, com_1, com_2, com_3]

# Define a function to determine the first banker
def determine_banker(): 
    first_banker = all_players[randint(0,3)]
    if first_banker == player:
        all_players[0] = player
        player.is_banker = True
        all_players[1] = com_1
        all_players[2] = com_2
        all_players[3] = com_3
                
    elif first_banker == com_1:
        all_players[0] = com_1
        com_1.is_banker = True
        all_players[1] = com_2
        all_players[2] = com_3
        all_players[3] = player
        
    elif first_banker == com_2:
        all_players[0] = com_2
        com_2.is_banker = True
        all_players[1] = com_3
        all_players[2] = player
        all_players[3] = com_1
               
    else:
        all_players[0] = com_3
        com_3.is_banker = True
        all_players[1] = player
        all_players[2] = com_1
        all_players[3] = com_2   
        
determine_banker()        
round_counter = 4

# Let's play the game.
while round_counter > 0 and player.wallet > 0:
    round_counter -= 1
    all_players[0].is_banker = True
    for x in all_players:
        x.point = 0
    banker_winloss = 0
    print "-" * 20
    print "%s has %s coins." % (all_players[0].name, all_players[0].wallet)
    print "%s is the banker. Everyone else, place your bets." % (all_players[0].name)
    print "-----"
    #sleep(0.5)
    for y in all_players: # All players that aren't the banker place their bets
        if y.is_banker == False:
            y.place_bet()
            print "-----"
            #sleep(0.2)

    # The banker rolls dice. Let's define instant win and instant lose conditions for the banker here. 
    all_players[0].banker_roll_dice()
    # Instant lose - no score, point 1, 1-2-3
    if all_players[0].point == 0 or all_players[0].point == 1 or all_players[0].point == 123:
        banker_loses = (all_players[1].bet + all_players[2].bet + all_players[3].bet)
        all_players[0].wallet -= banker_loses
        print "%s lost %s coins." % (all_players[0].name, banker_loses)
        print "----"
        for x in all_players:
            if x.is_banker == False:
                x.wallet += (x.bet)
                if x == player:
                    print "You won %s coins." % (x.bet)
                    print
    # Instant win - trips, 4-5-6, point = 6
    elif all_players[0].point == "trips" or all_players[0].point == 456 or all_players[0].point == 6:
        banker_wins = (all_players[1].bet + all_players[2].bet + all_players[3].bet)
        all_players[0].wallet += banker_wins
        print "%s won %s coins. Everyone else loses." % (all_players[0].name, banker_wins)
        print "-----"
        for x in all_players:
            if x.is_banker == False:
                x.wallet -= (x.bet)
                if x == player:
                    print "You lost %s coins." % (x.bet)
                    print

    # If the banker doesn't get an instant win/lose, players roll against the banker's point. 
    else:
        for x in all_players:            
            if x.is_banker == False:
                x.point = 0
                x.roll_dice()
                # If the non-banker rolls point 1 or no score...
                if x.point == 0 or x.point == 1 or x.point == 123:
                    banker_winloss += x.bet
                    all_players[0].wallet += x.bet
                    x.wallet -= x.bet
                    if x == player:
                        print "You lose this round. You lost %s coins." % (x.bet)
                        print
                    else:
                        print "%s loses this round. %s lost %s coins." % (x.name, x.name, x.bet)
                        print 
                    
                    #print banker_winloss #debug
                elif x.point == "trips" or x.point == 6 or x.point == 456:
                    x.wallet += x.bet
                    all_players[0].wallet -= x.bet
                    banker_winloss -= x.bet
                    if x == player:
                        print "You win! You won %s coins." % (x.bet)
                    else:
                        print "%s wins! %s won %s coins." % (x.name, x.name, x.bet)
                    print
                elif x.point != 0 and x.point != 1:
                    if x.point == all_players[0].point:
                        print "%s tied with the banker. No money won or lost." % (x.name)
                        print
                    elif x.point > all_players[0].point:
                        x.wallet += x.bet
                        all_players[0].wallet -= x.bet
                        banker_winloss -= x.bet
                        print "%s wins! %s won %s coins." % (x.name, x.name, x.bet)
                        print
                    else:
                        x.wallet -= x.bet
                        all_players[0].wallet += x.bet
                        banker_winloss += x.bet
                        print "%s lost to the banker. %s lost %s coins." % (x.name, x.name, x.bet)
                        #print banker_winloss #debug
                        print
        # After all calculations are made, display how much the banker won or lost.
        if banker_winloss == 0:
            print "The banker, %s, broke even this round." % (all_players[0].name)
        elif banker_winloss > 0:
            print "The banker, %s, won %s coins this round." % (all_players[0].name, banker_winloss)
        else:
            print "The banker, %s, lost %s coins this round." % (all_players[0].name, abs(banker_winloss))
        print
    # If anyone runs out of money, divine intervention gives them some spare change.
    for x in all_players:
        if x.wallet <= 0:
            x.wallet = 50
            print "Oh no! %s doesn't have any money. A chorus of divine voices is heard and 50 coins appear in %s's wallet." % (x.name, x.name)
            print

    # Change player order for the next round. 
    all_players[0].is_banker = False    
    all_players.insert(0, all_players[3])
    del all_players[4]
    if round_counter == 1:
        print "There is %s round remaining." % (round_counter)        
        print raw_input("Press enter to start the next round.")
    elif round_counter > 0:
        print "There are %s rounds remaining." % (round_counter)        
        print raw_input("Press enter to start the next round.")
    # Every four rounds, see if the player wants to continue.
    else:
        print "You have %s coins." % (player.wallet)
        play_again = raw_input("Play again? Y or N: ")
        print
        if play_again.lower() == 'y':
            round_counter = 4
        else:
            print "Thanks for playing CEE-LO by Psydungeon Laboratories. Goodbye!"
            print raw_input("Press enter to quit.")


