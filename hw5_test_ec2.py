import unittest
import hw5_cards_ec2


class TestHand(unittest.TestCase):

    def test_remove_pairs(self):
        '''
        Test that if you invoke the remove_pairs method on a Hand, the Hand will remove all pairs.

        '''

        c1 = hw5_cards_ec2.Card(1, 1)
        c2 = hw5_cards_ec2.Card(0, 2)
        c3 = hw5_cards_ec2.Card(3, 3)
        c4 = hw5_cards_ec2.Card(1, 2)
        c5 = hw5_cards_ec2.Card(0, 7)
        c6 = hw5_cards_ec2.Card(2, 3)
        c7 = hw5_cards_ec2.Card(1, 3)
        h1 = hw5_cards_ec2.Hand([c1, c2, c3, c4, c5, c6, c7])
        self.assertEqual(len(h1.init_cards), 7)
        h1.remove_pairs()
        self.assertEqual(len(h1.init_cards), 3)

    def test_deal(self):
        '''
        Test that if you invoke the deal method on the Deck, each hand will get the same card if b != -1;
        all of the cards should be dealt if the number of cards per hand is set to -1

        '''
        d1 = hw5_cards_ec2.Deck()
        d1.shuffle()
        list1 = d1.deal(4, 10)
        self.assertEqual(len(list1), 4)
        h1 = list1[0]
        self.assertEqual(len(h1.init_cards), 10)

        d2 = hw5_cards_ec2.Deck()
        d2.shuffle()
        list2 = d2.deal(7, -1)
        self.assertEqual(len(d2.cards), 0)


if __name__ == "__main__":
    unittest.main()

