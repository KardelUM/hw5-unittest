import unittest

from hw5_cards import Card
from hw5_cards_ec2 import Hand, Deck


class TestEC2(unittest.TestCase):
    def testRemove_paris(self):
        c1 = Card(0, 12)
        c2 = Card(1, 12)
        c3 = Card(3, 12)
        c4 = Card(0, 11)
        c5 = Card(1, 11)
        c6 = Card(0, 10)
        c7 = Card(1, 10)
        c8 = Card(1, 1)
        h = Hand([c1, c2, c3, c4, c5, c6, c7, c8])
        h.remove_pairs()

        self.assertEqual(len(h.cards), 2)
        self.assertEqual(h.cards[0].rank, 12)
        self.assertEqual(h.cards[0].suit, 3)
        self.assertEqual(h.cards[1].rank, 1)
        self.assertEqual(h.cards[1].suit, 1)

    def testDeal(self):
        testcases = [(10, 10, [6, 6, 5, 5, 5, 5, 5, 5, 5, 5]),  # normal testing
                     (13, 4, [4] * 13),
                     (10, -1, [6, 6, 5, 5, 5, 5, 5, 5, 5, 5]),
                     (10, 4, [4] * 10),
                     (10, -2, [0]*10),  # exception testing
                     (10, 0, [0]*10),
                     (-1, 2, []),
                     (0, 2, []),
                     ]
        for testcase in testcases:
            deck = Deck()
            hands = deck.deal(testcase[0], testcase[1])
            cardnumList = [len(hand.cards) for hand in hands]
            self.assertEqual(cardnumList, testcase[2])

if __name__ == "__main__":
    unittest.main()