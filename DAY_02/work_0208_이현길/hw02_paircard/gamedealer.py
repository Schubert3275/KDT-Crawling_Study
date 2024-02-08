from card import Card
import random

class GameDealer:
    def __init__(self) -> None:
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "♦"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in card_suits:
            for number in card_numbers:
                self.deck.append(Card(suit, number))

    def display_deck(self):
        print('-' * 100)
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        for i in range(len(self.deck)):
            print(self.deck[i], end=' ' if i % self.suit_number != self.suit_number-1 else '\n')
        print()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


if __name__ == "__main__":
    dealer = GameDealer()

    print("[GameDealer] 초기 카드 생성")
    dealer.make_deck()
    dealer.display_deck()
    print()

    print("[GameDealer] 카드 랜덤하게 섞기")
    dealer.shuffle_deck()
    dealer.display_deck()

    print('=' * 100)
