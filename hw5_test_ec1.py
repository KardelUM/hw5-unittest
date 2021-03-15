import unittest

from hw5_cards import Card, Deck
from hw5_cards_ec1 import Hand


class TestHand(unittest.TestCase):
    def testConstruction(self):
        c1 = Card(0, 1)
        c2 = Card(3, 2)
        outlier = "im outlier"
        h1 = Hand([c1, c2, outlier])
        self.assertIsInstance(Hand(None).cards, list)
        self.assertIsInstance(h1.cards, list)
        # the outlier will be filtered out
        self.assertEqual(len(h1.cards), 2)

        self.assertEqual(h1.cards[0], c1)
        self.assertIsInstance(h1.cards[0], Card)
        self.assertEqual(h1.cards[1], c2)
        self.assertIsInstance(h1.cards[1], Card)

    def testAddCard(self):
        c1 = Card(0, 1)
        c2 = Card(3, 2)
        h1 = Hand([c1, c2])
        h1.add_card(Card(3, 2))
        self.assertEqual(len(h1.cards), 2)
        h1 = Hand([c1, c2])
        h1.add_card(Card(2, 2))
        self.assertEqual(len(h1.cards), 3)
        h1 = Hand([c1, c2])
        h1.add_card("hello")
        self.assertEqual(len(h1.cards), 2)

    def testRemoveCard(self):
        c1 = Card(0, 1)
        c2 = Card(3, 2)
        h1 = Hand([c1, c2])
        r1 = h1.remove_card(Card(3, 2))
        self.assertEqual(len(h1.cards), 1)
        self.assertIsInstance(r1, Card)
        self.assertEqual(str(r1), str(c2))
        h1 = Hand([c1, c2])
        r2 = h1.remove_card(Card(2, 2))
        self.assertEqual(len(h1.cards), 2)
        self.assertEqual(r2, None)
        h1 = Hand([c1, c2])
        r3 = h1.remove_card("hello")
        self.assertEqual(len(h1.cards), 2)
        self.assertEqual(r3, None)

    def testDrawCard(self):
        h1 = Hand([])
        deck = Deck()
        h1.draw(deck)
        self.assertEqual(len(h1.cards), 1)
        c1 = Card(0, 1)
        c2 = Card(3, 2)
        deck = Deck()
        h1 = Hand([c1, c2])
        os = len(h1.cards)
        h1.draw(deck)
        self.assertEqual(len(h1.cards), os+1)


if __name__=="__main__":
    unittest.main()