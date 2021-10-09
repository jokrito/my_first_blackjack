############### Blackjack Project #####################
import random
from art import logo

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Deal card function
def deal_card():
  '''Function that deals one card each time it is called'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card_dealt = random.choice(cards)
  return card_dealt

def show_hands():
  print(f"Your hand: {player_hand}")
  print(f"Dealer's hand: {dealer_hand}")

# Returns the index of the first ace in a hand
def find_ace(whos_hand):
  ace_index = whos_hand.index(11)
  return ace_index
    
new_game = True

print(logo)
start = input("Would you like to play some Blackjack? 'y' or 'n' ")

# Complete game loop with restarts
while new_game:
  dealer_hand = []
  player_hand = []
  game_over = False

  # Deals initial hands and shows ONE of the dealers cards
  if start.lower() == "y":
    for t in range(2):
      player_hand.append(deal_card())
      dealer_hand.append(deal_card())

    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: [{dealer_hand[0]}]")

    # Check for BlackJack
    if sum(player_hand) == 21 and len(player_hand) == 2:
        print("Blackjack! You win!")
        game_over = True
    elif sum(dealer_hand) == 21 and len(dealer_hand) == 2:
        print("Dealer has Blackjack! You lose...")
        game_over = True

        # Game loop until one of the players bust
    while not game_over:
        new_card = input("Would you like another card? ")

          # Gives player option to draw cards until bust.
        if new_card.lower() == "y":
          player_hand.append(deal_card())
          print(player_hand)
          if sum(player_hand) > 21 and 11 in player_hand:
            player_hand[find_ace(player_hand)] = 1;
          elif sum(player_hand) > 21:
            game_over = True
            print("You bust! Game over")      
        elif new_card.lower() == "n":

          #Player is done. Dealer draws until 17 or bust
          while sum(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            if sum(dealer_hand) > 21 and 11 in dealer_hand:
              dealer_hand[find_ace(dealer_hand)] = 1
            elif sum(dealer_hand) > 21:            
              print("Dealer busts! You win!")
              game_over = True
              show_hands()

          # Hand comparison to determine winner
        elif sum(dealer_hand) > sum(player_hand):
          print("Dealer wins!") 
          game_over = True
          show_hands()
        elif sum(dealer_hand) == sum(player_hand):
          print("It's a draw!")
          game_over = True
          show_hands()
        elif sum(dealer_hand) < sum(player_hand):
          print("Player wins!")
          game_over = True  
          show_hands()

    # Ends game or restarts
    else:
      play_again = input("Would you like to play again? 'y' or 'n': ")
      if play_again.lower() == "n":
        new_game = False
        print("Have a nice day!")
      elif play_again.lower() == "y":
        new_game = True

  # If player chose 'n' at the initial invitation to play
  elif start.lower() == "n":
    new_game = False
    print("Have a nice day!")
