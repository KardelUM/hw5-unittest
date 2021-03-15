
# create the Hand with an initial set of cards
import random

from hw5_cards import Card


class Hand:
    '''a hand for playing card
    Class Attributes
    ----------------
    None
    Instance Attributes
    -------------------
    init_card: list
    a list of cards
    '''

    def __init__(self, init_cards):
        self.cards = []
        if init_cards is None:
            return
        for card in init_cards:
            if isinstance(card, Card):
                self.cards.append(card)

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand
        Parameters
        -------------------
        card: instance
        a card to add
        Returns
        -------
        None
        '''
        if not isinstance(card, Card):
            return
        if str(card) in [str(c) for c in self.cards]:
            return
        else:
            self.cards.append(card)

    def remove_card(self, card):
        '''remove a card from the hand
        Parameters
        -------------------
        card: instance
        a card to remove
        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        if not isinstance(card, Card):
            return None
        if str(card) not in [str(c) for c in self.cards]:
            return None
        else:
            i = [str(c) for c in self.cards].index(str(card))
            cardi = self.cards[i]
            self.cards = self.cards[:i] + self.cards[i + 1:]
            return cardi

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        Parameters
        -------------------
        deck: instance
        a deck from which to draw
        Returns
        -------
        None
        '''
        if not isinstance(deck, Deck):
            return
        card = deck.deal_card()
        self.add_card(card)

    def remove_pairs(self):
        ranks = [card.rank for card in self.cards]
        for i, r1 in enumerate(ranks):
            newRanks = ranks[:i]+ranks[i+1:]
            if r1 in newRanks:
                j = newRanks.index(r1)+1
                self.cards = self.cards[:i] + self.cards[i+1:j] + self.cards[j+1:]
                self.remove_pairs()
                break


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)  # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck

        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, nHands, nCards_per_hands):
        hands = []
        if nHands > 0:
            for _ in range(nHands):
                hands.append(Hand([]))
        else:
            return hands
        if nCards_per_hands < -1:
            return hands
        if nCards_per_hands == -1 or nCards_per_hands * nHands >= len(self.cards):
            player = 0
            while len(self.cards) != 0:
                hands[player].draw(self)
                player = (player+1) % nHands
            return hands
        if nCards_per_hands == 0:
            return hands
        if nCards_per_hands > 0 and nCards_per_hands * nHands < len(self.cards):
            player = 0
            for i in range(nCards_per_hands * nHands):
                hands[player].draw(self)
                player = (player + 1) % nHands
            return hands
