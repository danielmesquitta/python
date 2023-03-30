import random


def shuffle_deck(deck):
    random.shuffle(deck)


def deal_card(deck):
    return deck.pop()


def hand_value(hand):
    total = sum(card[1] for card in hand)
    aces = [card for card in hand if card[0] == "Ace"]
    for ace in aces:
        if total > 21:
            total -= 10
    return total


def display_hand(hand):
    return ", ".join(card[0] for card in hand)


def play_game():
    deck = [("Ace", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7),
            ("8", 8), ("9", 9), ("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]

    shuffle_deck(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        print(
            f"\nPlayer's hand: {display_hand(player_hand)} | Total: {hand_value(player_hand)}")

        print(
            f"Dealer's hand: {dealer_hand[0][0]} | Total: {hand_value([dealer_hand[0]])}")

        choice = input("Hit or stand? ").lower()

        if choice == "hit":
            player_hand.append(deal_card(deck))

            if hand_value(player_hand) > 21:
                print("Player busts!")
                return False

        elif choice == "stand":
            break

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print(
        f"\nPlayer's hand: {display_hand(player_hand)} | Total: {hand_value(player_hand)}")

    print(
        f"Dealer's hand: {display_hand(dealer_hand)} | Total: {hand_value(dealer_hand)}")

    if hand_value(dealer_hand) > 21:
        print("Dealer busts!")
        return True

    elif hand_value(dealer_hand) >= hand_value(player_hand):
        print("Dealer wins!")
        return False

    else:
        print("Player wins!")
        return True


while True:
    print("Welcome to Blackjack!")
    if play_game():
        print("You win!")

    else:
        print("You lose!")

    play_again = input("Play again? (y/n) ").lower()

    if play_again != "y":
        break
