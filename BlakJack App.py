class Card():
    """ Simulate a single card with rank, value,and suit"""

    def __init__(self,rank,value,suit):
        """Initialze card attributes"""
        self.rank=rank
        self.value=value
        self.suit=suit
    def display_card(self):
        """Show the rank and suit of individual card"""
        print(self.rank+" of "+self.suit)

class Deck():
    """Simulate a deck of 52 individual playing cards"""

    def __init__(self):
        """Initialze deck attributes """
        self.cards=[]

    def buiild_deck(self):
        suits=['Hearts','Diamonds','Spades','Clubs']
        ranks={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
               '10':10,'J':10,'Q':10,'K':10,'A':11,}

        for suit in suits:
            for rank,value in ranks.items():
                card=Card(rank,value,suit)
                self.cards.append(card)


class Player():
    pass
class Dealer():
    pass
class Game():
    pass