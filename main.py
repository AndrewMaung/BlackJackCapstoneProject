import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True
flag = True  # Define the flag variable at the top
busted = False

def deals():
    """
    Deals two unique cards to the player and the computer.
    Returns the player's and computer's cards as lists.
    """
    player_deal = random.sample(cards, k=2)
    computer_deal = random.sample(cards, k=2)
    return player_deal, computer_deal

while continue_game:                                                                       
    player_deck, computer_deck = deals() 
    print("Your cards are:")
    print(player_deck)

    while sum(player_deck) < 21:
        print("What will be your choice")
        print("[1] Stand: You will not draw another card")
        print("[2] Hit: You will be drawing a card")
        player_choice = int(input("Enter 1 for Stand and 2 for Hit: "))

        if player_choice == 1:
            break
        elif player_choice == 2:
            while True:
                new_element = random.choice(cards)
                if new_element not in player_deck:
                    break
            player_deck.append(new_element)
            print("Your deck is now", player_deck)
        else:
            print("Invalid choice. Please enter 1 for Stand and 2 for Hit.")

    print("Your final deck is", player_deck)
    if sum(player_deck) > 21:
        print("You went over 21! BUSTED")
        busted = True

    while sum(computer_deck) < 17:
        new_element = random.choice(cards)
        computer_deck.append(new_element)
        if sum(computer_deck) > 21:
            print("Dealer Busts! You Win")
            flag = False

    if not flag:
        break
    
    print("Dealer's final deck is", computer_deck)

    player_result = sum(player_deck)
    dealer_result = sum(computer_deck)
    
    if busted == False:
        if player_result > dealer_result:
            print(f"Your cards add up to {player_result} and the dealer's cards add up to {dealer_result}")
            print("YOU WIN!")
        else:
            print(f"Your cards add up to {player_result} and the dealer's cards add up to {dealer_result}")
            print("YOU LOSE")
    else:
        print("You Lose!")
    
    replay = input("Do you want to continue the game? (y/n): ")
    if replay != 'y':
        continue_game = False
        print("END")

