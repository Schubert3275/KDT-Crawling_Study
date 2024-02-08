from card import Card
from player import Player
from gamedealer import GameDealer

def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")
    dealer = GameDealer()
    dealer.make_deck()
    dealer.shuffle_deck()

    num = 10
    while len(dealer.deck) != 0:
        print('=' * 100)
        print(f'카드 나누어 주기: {num}장')
        for i in range(num):
            player1.add_card_list(dealer.deal_card())
            player2.add_card_list(dealer.deal_card())
        dealer.display_deck()
        print('=' * 100)
        player1.display_two_card_lists()
        num = 4




if __name__ == "__main__":
    play_game()
