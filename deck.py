import random


class Deck :
    def __init__(self):
        self.suits = ["heart", "diamond", "spade", "club"]
        self.ranks = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "ace", "king", "queen", "jack"]
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                card = f"{rank} of {suit}"
                self.cards.append(card)

        random.shuffle(self.cards)

    def deal_cards(self):
        half = 26
        player1 = self.cards[:half]
        player2 = self.cards[half:]
        return player1, player2

