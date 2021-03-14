# create the Hand with an initial set of cards
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
        self.init_cards = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters
        ------------
        card: instance
            a card to add

        Returns
        -------
        None

        '''

        card_strs = []
        for c in self.init_cards:
            card_strs.append(c.__str__())
        if card.__str__() not in card_strs:
            self.init_cards.append(card)

    def remove_card(self, card):
        '''remove a card from the hand

        Parameters
        -----------------
        card: instance
            a card to remove

        Returns
        -------
        the card, or None if the card was not in the Hand

        '''

        card_strs = []
        for c in self.init_cards:
            card_strs.append(c.__str__())
        if card.__str__() not in card_strs:
            return None
        else:
            index1 = card_strs.index(card.__str__())
            self.init_cards.pop(index1)
            return card

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card

        Parameters
        ------------------
        deck: instance
            a deck from which to draw

        Returns
        -------
        None

        '''

        if len(deck.cards) == 0:
            print("The deck is empty! You can't draw a card.")
            return None
        else:
            card = deck.cards[-1]
            deck.cards.pop(-1)
            card_strs = []
            for c in self.init_cards:
                card_strs.append(c.__str__())
            if card.__str__() not in card_strs:
                self.init_cards.append(card)
            if len(deck.cards) == 0:
                print("The deck is empty now! You can't draw a card next time.")
            return None

