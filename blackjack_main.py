import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + "of" + self.suit

class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in suits :
            for rank in ranks :
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck :
            deck_comp = deck_comp + '\n' + card.__str__()
        return "The deck has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        removed_card_obj = self.deck.pop()
        return removed_card_obj

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        # Find if the card is an ace
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):

        while self.value > 21 and self.aces > 0 :

            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet

# Seperate Functions
def take_bet(chips):
    while True :
        try :
            chips.bet = int(input('How many chips would you like to bet :'))
        except :
            print('Sorry..Provide proper Intezer')
        else :
            if chips.bet > chips.total :
                print('Sorry..,you dont have enough chips. You have : '. format(chips.total))
            else :
                break

def hit(hand,deck):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_aces()

def hit_or_stand(deck,hand) :
    global playing
    while True :
        x = input('Hit or stand Enter h or s')
        if x[0].lower()=='h':
            hit(hand,deck)
        elif x[0].lower()=='s':
            print('Player stands Dealers Turn')
            playing = False
        else :
            print('Sorry i did not understand that. Please enter h or s')
            continue
        break

def player_busts(player,dealer,chips):
    print('Bust Player')
    chips.loose_bet()

def player_wins(player,dealer,chips):
    print('Player Wins')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Bust Dealer and Player Wins')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins')
    chips.loose_bet()

def push(player,dealer):
    print('Dealer and Player Tie!!')


if __name__ == '__main__':
    deck_obj = Deck()
    print(deck_obj)
    deck_obj.shuffle()
    print(deck_obj)
    print(deck_obj.deal())
    card_obj = Card()
    print(card_obj)
