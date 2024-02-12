from card import Card
import random


class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in card_suits:
            for num in card_numbers:
                self.deck.append(Card(suit, num))
        print(f'[GameDealer] 초기 카드 생성')
        self.print_deck()

        print(f'[GameDealer]카드 랜던하게 섞기')
        random.shuffle(self.deck)
        self.print_deck()

    def distribute_card(self, num):
        print()
        print('=' * 60)
        print(f'카드 나누어 주기: {num}장')
        card_list1 = list()
        card_list2 = list()

        for i in range(num):
            card_list1.append(self.deck.pop())
            card_list2.append(self.deck.pop())

        self.print_deck()
        return card_list1, card_list2

    def print_deck(self):
        print('-' * 60)
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        for i in range(len(self.deck)):
            print(self.deck[i], end=' ')
            if (i + 1) % self.suit_number == 0:
                print()
        print()
