import unittest
import hw5_cards_ec1
import hw5_cards


class TestHand(unittest.TestCase):

    def test_construct_Hand(self):
        c1 = hw5_cards.Card(1, 1)
        c2 = hw5_cards.Card(0, 2)
        h1 = hw5_cards_ec1.Hand([c1, c2])

        self.assertIsInstance(h1.init_cards, list)

    def test_add_card(self):
        '''
        Test that if you invoke the add_card method on a Hand, the Hand has one more cards in it afterwards.
        Test that if you invoke the add_card method with a card that is already in the Hand, the Hand size is not affected.

        '''

        c1 = hw5_cards.Card(1, 1)
        c2 = hw5_cards.Card(0, 2)
        c3 = hw5_cards.Card(3, 3)
        c4 = hw5_cards.Card(0, 2)
        h1 = hw5_cards_ec1.Hand([c1, c2])
        self.assertEqual(len(h1.init_cards), 2)
        h1.add_card(c3)
        self.assertEqual(len(h1.init_cards), 3)
        h1.add_card(c4)
        self.assertEqual(len(h1.init_cards), 3)

    def test_remove_card(self):
        '''
        Test that if you invoke the remove_card method on a Hand, the Hand has one fewer cards in it afterwards.
        Test that if you invoke the remove_card method with a Hand that is not in the Hand, the Hand size is not affected.

        '''

        c1 = hw5_cards.Card(1, 1)
        c2 = hw5_cards.Card(0, 2)
        c3 = hw5_cards.Card(0, 2)
        c4 = hw5_cards.Card(3, 3)
        h1 = hw5_cards_ec1.Hand([c1, c2])
        self.assertEqual(len(h1.init_cards), 2)
        h1.remove_card(c3)
        self.assertEqual(len(h1.init_cards), 1)
        h1.remove_card(c4)
        self.assertEqual(len(h1.init_cards), 1)

    def test_draw(self):
        '''
        Test that if you invoke the draw method from a deck and add it to the hand, the Hand has one more cards in it afterwards.
        Test that if you invoke the draw method with a Hand that caused a side effect: the deck will be depleted by one card.

        '''

        c1 = hw5_cards.Card(1, 1)
        c2 = hw5_cards.Card(0, 2)
        d1 = hw5_cards.Deck()
        h1 = hw5_cards_ec1.Hand([c1, c2])
        self.assertEqual(len(h1.init_cards), 2)
        self.assertEqual(len(d1.cards), 52)
        h1.draw(d1)
        self.assertEqual(len(h1.init_cards), 3)
        self.assertEqual(len(d1.cards), 51)

        d2 = hw5_cards.Deck()
        self.assertEqual(len(d2.cards), 52)
        for i in range(len(d2.cards)-1):
            d2.cards.pop(-1)
        h1.draw(d2)
        self.assertEqual(len(h1.init_cards), 4)
        self.assertEqual(len(d2.cards), 0)


if __name__ == "__main__":
    unittest.main()

