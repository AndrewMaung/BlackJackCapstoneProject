import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deals():
    """
    Deals two unique cards to the player and the computer.
    Returns the player's and computer's cards as lists.
    """
    player_deal = random.sample(cards,k=2)
    computer_deal = random.sample(cards, k=2)
    return player_deal,computer_deal

#Display to the player his deck
player_deck, _ = deals() 
print("Your cards is: ")
print(player_deck)

player_deck, _ = deals() 
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
