import random

# list of the card in the game change to your cards (trump card etc...)
card_list = ["AS_pique", "AS_coeur", "AS_carreau", "AS_trefle", "AS__pique", "AS__coeur", "AS__carreau", "AS__trefle",
             "2_pique", "2_coeur", "2_carreau", "2_trefle", "2__pique", "2__coeur", "2__carreau", "2__trefle",
             "3_pique",
             "3_coeur", "3_carreau", "3_trefle", "3__pique", "3__coeur", "3__carreau", "3__trefle", "4_pique",
             "4_coeur",
             "4_carreau", "4_trefle", "4__pique", "4__coeur", "4__carreau", "4__trefle", "5_pique", "5_coeur",
             "5_carreau",
             "5_trefle", "5__pique", "5__coeur", "__carreau", "5__trefle", "6_pique", "6_coeur", "6_carreau",
             "6_trefle",
             "6__pique", "6__coeur", "6__carreau", "6__trefle", "7_pique", "7_coeur", "7_carreau", "7_trefle",
             "7__pique",
             "7__coeur", "7__carreau", "7__trefle", "8_pique", "8_coeur", "8_carreau", "8_trefle", "8__pique",
             "8__coeur",
             "8__carreau", "8__trefle", "9_pique", "9_coeur", "9_carreau", "9_trefle", "9__pique", "9__coeur",
             "9__carreau",
             "9__trefle", "10_pique", "10_coeur", "10_carreau", "10_trefle", "10__pique", "10__coeur", "10__carreau",
             "10__trefle", "VALET_pique", "VALET_coeur", "VALET_carreau", "VALET_trefle", "VALET__pique",
             "VALET__coeur",
             "VALET__carreau", "VALET__trefle", "DAME_pique", "DAME_coeur", "DAME_carreau", "DAME_trefle",
             "DAME__pique",
             "DAME__coeur", "DAME__carreau", "DAME__trefle", "ROI_pique", "ROI_coeur", "ROI_carreau", "ROI_trefle",
             "ROI__pique", "ROI__coeur", "ROI__carreau", "ROI__trefle"]
player_nmbr = {"player1": [], "player2": []}  # list of player
card_distributed = 7  # number of card distributed change depending on your game
fin = ""


def card():
    """Function that distributes the cards to each player
    depending on the number of players and cards to distribute written higher up"""
    for player_name in player_nmbr:
        for _ in range(card_distributed):
            # take a random number
            temp = random.randint(0, len(card_list) - 1)
            # add it to the player list
            player_nmbr[player_name].append(card_list[temp])
            # then remove it from the card list
            card_list.pop(temp)

    for player_name, cards in player_nmbr.items():
        print("Player", player_name, "has cards:", cards)


def pioche():
    """Function that allow you to draw a card """
    for draw in player_nmbr:
        # ask if the player take a card
        choix = input(f"Voulez-vous piocher, {draw} ? (y/n): ")
        if choix.lower() == 'y':
            card_2_draw = random.randint(0, len(card_list) - 1)
            player_nmbr[draw].append(card_list[card_2_draw])
            card_list.pop(card_2_draw)

    for player_name, cards in player_nmbr.items():
        print("Player", player_name, "has cards:", cards)


def utilise():
    """fonction that make you use a card """
    for used in player_nmbr:
        # ask what card the player has lost
        carte_utilise = int(input("quelle carte avez vous perdu (son nombre en partant de 1): "))
        # delete the card from the player card list
        player_nmbr[used].pop(carte_utilise - 1)
    # show the player card list
    for player_name, cards in player_nmbr.items():
        print("Player", player_name, "has cards:", cards)


card()
while fin.lower() != "y":
    utilise()
    pioche()
    fin = input(f"fin ? (y/n): ")
