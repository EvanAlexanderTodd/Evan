from random import randint
import time

card_number = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_type = ["Spades", "Hearts", "Clubs", "Diamonds"]
deck = []
deck_values = {}
player_hand = []
dealer_hand = []
split_hand = []
all_hands = {}
player_total = 0
dealer_total = 0
winning_hands = 0
drawing_hands = 0
losing_hands = 0
dealer_blackjack = 0
bet = 0
coins = 10
split_game = False
for y in range(0, (len(card_values))):
        deck_values[(card_number[y])] = card_values[y]

def new_game():
    response = ""
    while response != "y":
            print("Are you ready to play blackjack? y/n: ")
            response = input()
    while response == "y":
        global player_total, winning_hands, drawing_hands, losing_hands, dealer_blackjack, split_game, bet, dealer_total, split_bet
        deck.clear()
        player_hand.clear()
        dealer_hand.clear()
        player_total = 0
        dealer_total = 0
        winning_hands = 0
        drawing_hands = 0
        losing_hands = 0
        dealer_blackjack = 0
        bet = 0
        split_game = False
        bet = "a"
        while bet.isdigit() == False:
            if coins > 0:
                time.sleep(0.5)
                print("\nPlease place your bet. You can bet a whole number (no decimals) up to " + str(coins) + " coins.\n")
                bet = input()
        bet = float(bet)
        split_bet = bet
        if bet <= coins and bet >= 1:
            time.sleep(0.5)
            print("\nBet accepted, let's begin!\n")
            new_deck()
            draw_hands()
            dealer_turn()
            split()
            results()
            print("\nYou have " + str(coins) + " coins.")
            response = ""
            while response != "y" and response != "n":
                print("Would you like to play again? y/n: ")
                response = input()
                if response == "n":
                    print("You ended the game with " + str(coins) + " coins. Thank you for playing!")
                    return 0
        elif bet > coins:
            time.sleep(0.5)
            print("Oops, that's too much! Try again.")
        elif bet < 1:
            time.sleep(0.5)
            print("Oops, that's not enough! Minimum bet is 1 coin.")
        else:
            time.sleep(0.5)
            print("Sorry, you don't have enough coins to play :( .")
            break        


def new_deck():
    for i in card_type:
        for x in card_number:
            deck.append(x + " of " + i)
            deck.append(x + " of " + i)

def draw_hands():
    while len(player_hand) < 2:
        x = randint(0, (len(deck) - 1))
        player_hand.append(deck[x])
        deck.pop(x)
        y = randint(0, (len(deck) - 1))
        player_hand.append(deck[y])
        deck.pop(y)
    while len(dealer_hand) < 2:
        x = randint(0, (len(deck) - 1))
        dealer_hand.append(deck[x])
        deck.pop(x)
        y = randint(0, (len(deck) - 1))
        dealer_hand.append(deck[y])
        deck.pop(y)

def dealer_turn():
    global dealer_total, winning_hands
    for i in range(0, 2):
        if "Ace" in dealer_hand[i].split():
            dealer_ace()
            return 0
        else:
            for card in card_number:
                if card in dealer_hand[i].split():
                    dealer_total = dealer_total + deck_values[card]
    while dealer_total < 17:
        x = randint(0, (len(deck) - 1))
        dealer_hand.append(deck[x])
        deck.pop(x)
        if "Ace" in dealer_hand[(len(dealer_hand) - 1)].split():
            if dealer_total <= 10:
                dealer_ace()
                return 0
            else:
                dealer_total = dealer_total + 1
        else:
            for card in card_number:
                if card in dealer_hand[(len(dealer_hand) - 1)].split():
                    dealer_total = dealer_total + deck_values[card]
    return dealer_total

def dealer_ace():
    global ace_low, dealer_total, ace_high
    ace_low = 0
    ace_high = 0
    for i in range(0, len(dealer_hand)):
        if "Ace" in dealer_hand[i].split():
            ace_low = ace_low + 1
            if ace_high <= 10:
                ace_high = ace_high + 11
            else:
                ace_high = ace_high + 1
        else:
            for card in card_number:
                if card in dealer_hand[i].split():
                    ace_low = ace_low + deck_values[card]
                    ace_high = ace_high + deck_values[card]
    if ace_high >= 18 and ace_high <= 21:
        dealer_total = ace_high
        return dealer_total
    else:                
        while ace_high <= 17:
            x = randint(0, (len(deck) - 1))
            dealer_hand.append(deck[x])
            deck.pop(x)
            for card in card_number:
                if card in dealer_hand[(len(dealer_hand) - 1)].split():
                    ace_low = ace_low + deck_values[card]
                    ace_high = ace_high + deck_values[card]
        if ace_high >= 18 and ace_high <= 21:
            dealer_total = ace_high
            return dealer_total
        while ace_low < 17 and ace_high > 21:
            x = randint(0, (len(deck) - 1))
            dealer_hand.append(deck[x])
            deck.pop(x)
            for card in card_number:
                if card in dealer_hand[(len(dealer_hand) - 1)].split():
                    ace_low = ace_low + deck_values[card]
    dealer_total = ace_low
    return dealer_total


def player_turn():
    global player_total
    for i in range(0, 2):
        if "Ace" in player_hand[i].split():
            player_ace()
            return 0
        else:
            for card in card_number:
                if card in player_hand[i].split():
                    player_total = player_total + deck_values[card]
    stick_or_hit()



def player_ace():
    global player_total, coins, bet, player_low, player_high, losing_hands, winning_hands, drawing_hands, dealer_blackjack, player_hand
    player_low = 0
    player_high = 10
    for j in range(0, 2):
        if "Jack" in player_hand[j].split() or "Queen" in player_hand[j].split() or "King" in player_hand[j].split() or "10" in player_hand[j].split():
            time.sleep(0.5)
            print("Blackjack! You win " + str(bet * 1.5) + " coins!")
            coins = coins + (bet * 1.5)
            return 0
        else:
            for card in card_number:
                if card in player_hand[j].split():
                    player_low = player_low + deck_values[card]
                    player_high = player_high + deck_values[card]
    while player_low <= 21:
        if player_high <= 21:
            print("Current total: " + str(player_low) + " or " + str(player_high))
        elif player_high > 21:
            print("Current total: " + str(player_low))
        time.sleep(1)
        print("Would you like to stick or hit?")
        response = input()
        x = randint(0, (len(deck) - 1))
        if response.lower() == "stick":
            time.sleep(1)
            print("\nYour final hand is: ")
            for i in range(0, len(player_hand)):
                print(player_hand[i])
            if player_high <= 21:
                print("\nFinal total: " + str(player_high))
                player_total = player_high
                if dealer_total == 21 and len(dealer_hand) == 2:
                    dealer_blackjack += 1
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
                elif dealer_total > 21 and player_high <= 21:
                    winning_hands += 1
                    #all_hands["Won"] = player_hand
                elif player_high > dealer_total:
                    winning_hands += 1
                    #all_hands["Won"] = player_hand
                elif player_high == dealer_total:
                    drawing_hands += 1
                    #all_hands["Drew"] = player_hand
                elif player_high < dealer_total:
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
            elif player_high > 21:
                print("\nFinal total: " + str(player_low))
                player_total = player_low
                if dealer_total == 21 and len(dealer_hand) == 2:
                    dealer_blackjack += 1
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
                elif dealer_total > 21 and player_low <= 21:
                    winning_hands += 13
                    #all_hands["Won"] = player_hand
                elif player_low > dealer_total:
                    winning_hands += 1
                    #all_hands["Won"] = player_hand
                elif player_low == dealer_total:
                    drawing_hands += 1
                    #all_hands["Drew"] = player_hand
                elif player_low < dealer_total:
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
            return 0
        elif response.lower() == "hit":
            player_hand.append(deck[x])
            deck.pop(x)
            print("\n")
            print(player_hand[(len(player_hand) - 1)])
            for card in card_number:
                if card in player_hand[(len(player_hand) - 1)].split():
                    player_low = player_low + deck_values[card]
                    player_high = player_high + deck_values[card]
        else:
            print("Oops, I didn't catch that.")
    
    time.sleep(1)
    print("Looks like you went bust! You lose " + str(bet) + " coins!")
    coins = coins - bet
    player_total = 0
    player_hand = []
    return 0
               


def stick_or_hit():
    global player_total, dealer_blackjack, losing_hands, drawing_hands, winning_hands, bet, coins, player_hand
    while len(player_hand) > 0 or len(split_hand) > 0:
        while player_total < 21:
            print("Current total: " + str(player_total))
            time.sleep(1)
            print("Would you like to stick or hit?")
            response = input()
            x = randint(0, (len(deck) - 1))
            if response.lower() == "stick":
                time.sleep(1)
                print("\nYour final hand is: ")
                for i in range(0, len(player_hand)):
                    print(player_hand[i])
                print("\nFinal total: " + str(player_total))
                if dealer_total == 21 and len(dealer_hand) == 2:
                    dealer_blackjack += 1
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
                elif dealer_total > 21 and player_total <= 21:
                    winning_hands += 1
                    #all_hands["Won"] = player_hand
                elif player_total > dealer_total:
                    winning_hands += 1
                    #all_hands["Won"] = player_hand
                elif player_total == dealer_total:
                    drawing_hands += 1
                    #all_hands["Drew"] = player_hand
                elif player_total < dealer_total:
                    losing_hands += 1
                    #all_hands["Lost"] = player_hand
                return 0
            elif response.lower() == "hit":
                player_hand.append(deck[x])
                deck.pop(x)
                print("\n")
                print(player_hand[(len(player_hand) - 1)])
                for card in card_number:
                    if card in player_hand[(len(player_hand) - 1)].split():
                        player_total = player_total + deck_values[card]
            else:
                print("Oops, I didn't catch that.")
    
        time.sleep(1)
        print("Looks like you went bust! You lose " + str(bet) + " coins!")
        coins = coins - bet
        player_total = 0
        player_hand = []
        return 0


def win_draw_lose():
    global coins
    if dealer_blackjack > 0:
        print("Dealer has blackjack, you lose!")
        if split_bet > bet:
            coins = coins - split_bet
        else:
            coins = coins - bet
        return 0
    else:    
        if winning_hands > 0:
            print("You won " + str(winning_hands) + " hand(s)")
            coins = coins + (bet * winning_hands)
        if drawing_hands > 0:
            print("You drew " + str(drawing_hands) + " hand(s)")
        if losing_hands > 0:
            print("You lost " + str(losing_hands) + " hand(s)")
            coins = coins - (bet * losing_hands)
    #for key, value in all_hands.items():
        #print(key, ' : ', value)



def split():
    global split_game, bet, split_bet
    time.sleep(1)
    print("Your hand is: " + player_hand[0] + " + " + player_hand[1])
    print("\nDealer's first card is: " + dealer_hand[0])
    for card in card_number:
        if card in player_hand[0].split() and card in player_hand[1].split():
            if coins >= bet + split_bet:
                player_split = ""
                while player_split != "y" and player_split != "n":
                    print("Looks like you can split! Would you like to split? (You will have to double your bet) y/n: ")
                    player_split = input()
                    if player_split == "y":
                        split_bet = split_bet + bet
                        split_game = True
                        split_yes()
                        return 0
                    elif player_split != "y" and player_split != "n":
                        print("Sorry, I didn't catch that.")
    player_turn()

def split_yes():
    global player_hand, split_hand, player_total
    for i in range(0, 2):
        split_hand.append(player_hand[i])
    player_hand.clear()
    if len(split_hand) == 2:
        for i in range(0, 2):
            player_hand.append(split_hand[0])
            split_hand.pop(0)
            player_total = 0
            while len(player_hand) < 2:
                x = randint(0, (len(deck) - 1))
                player_hand.append(deck[x])
                deck.pop(x)
            split()
            player_hand.clear()
    else:
        player_hand.append(split_hand[0])
        split_hand.pop(0)
        player_total = 0
        while len(player_hand) < 2:
            x = randint(0, (len(deck) - 1))
            player_hand.append(deck[x])
            deck.pop(x)
        split()
        player_hand.clear()


def results():
    if (winning_hands + losing_hands + drawing_hands) > 0:
        time.sleep(1)
        print("\nThe dealer's hand is: \n")
        for i in range(0, len(dealer_hand)):
            time.sleep(1.5)
            print(dealer_hand[i])
        print("Dealer total: " + str(dealer_total))
        win_draw_lose()


new_game()
