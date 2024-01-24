import functions

play = True

while play:

    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if new_game == 'y':
        functions.play_game()
    else:
        play = False
