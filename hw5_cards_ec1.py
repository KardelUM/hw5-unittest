
# create the Hand with an initial set of cards
from hw5_cards import Card, Deck


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


