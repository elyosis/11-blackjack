import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    clear()
    print(logo)

    player_cards = []
    dealer_cards = []
    player_cards = deal_cards(player_cards, 2)
    dealer_cards = deal_cards(dealer_cards, 2)

    if calculate_score(dealer_cards) == 21 and len(dealer_cards) == 2:
        display_hands(player_cards, dealer_cards, True)
        print("Your opponent got a blackjack. You lose.")
        return
    elif calculate_score(player_cards) == 21 and len(player_cards) == 2:
        display_hands(player_cards, dealer_cards, True)
        print("You got a blackjack. It's your win!")
        return

    player_cards = player_turn(player_cards, dealer_cards)
    player_score = calculate_score(player_cards)

    if player_score > 21:
        display_hands(player_cards, dealer_cards, True)
        print("You went over. You lose.")
        return

    dealer_cards = dealer_turn(dealer_cards)
    dealer_score = calculate_score(dealer_cards)

    if dealer_score > 21:
        display_hands(player_cards, dealer_cards, True)
        print("You win!")
        return
    elif player_score == dealer_score:
        display_hands(player_cards, dealer_cards, True)
        print("It's a draw.")
        return
    elif player_score > dealer_score:
        display_hands(player_cards, dealer_cards, True)
        print("You win!")
        return
    else:
        display_hands(player_cards, dealer_cards, True)
        print("You lose.")
        return


def deal_cards(current_hand, amount):
    for n in range(amount):
        current_hand.append(random.choice(cards))

    return current_hand


def display_hands(player_hand, dealer_hand, is_final):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if is_final:
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    else:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {dealer_hand[0]}")


def calculate_score(hand):
    score = sum(hand)

    if score > 21 and 11 in hand:
        for aces in range(hand.count(11)):
            score -= 10

    return score


def player_turn(player_hand, dealer_hand):
    player_cards = player_hand
    continue_turn = True

    while continue_turn:
        display_hands(player_cards, dealer_hand, False)

        continue_round = input("Type 'y' to get another card, type 'n' to pass: ")

        if continue_round == "y":
            player_cards = deal_cards(player_cards, 1)
            player_score = calculate_score(player_cards)

            if player_score > 21:
                break
        else:
            continue_turn = False

    return player_cards


def dealer_turn(dealer_hand):
    dealer_cards = dealer_hand
    dealer_score = calculate_score(dealer_cards)

    if dealer_score < 17:
        dealer_cards = deal_cards(dealer_cards, 1)
        dealer_turn(dealer_cards)

    return dealer_cards
