from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")
    dealer = GameDealer()

    dealer.make_deck()

    num = 10
    count = 1
    winner = 0
    while len(dealer.deck) != 0:
        dealer.shuffle_deck()  # 매 단계마다 딜러 덱 셔플
        print(f'[{count}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
        print('=' * 100)
        print(f'카드 나누어 주기: {num}장')

        # 처음엔 10장, 두번째부터는 4장씩 배부
        for i in range(num):
            player1.add_card_list(dealer.deal_card())
            player2.add_card_list(dealer.deal_card())
        dealer.display_deck()

        # 첫번째 플레이어 카드 표시
        player1.check_one_pair_card()
        player1.display_two_card_lists()
        player1.display_hand_card_list()

        # 두번째 플레이어 카드 표시
        player2.check_one_pair_card()
        player2.display_two_card_lists()
        player2.display_hand_card_list()

        num = 4
        count += 1
        # 승패 판별
        if len(player1.holding_card_list) == 0 and len(player2.holding_card_list) == 0:
            break
        elif len(player1.holding_card_list) == 0:
            winner = 1
            break
        elif len(player2.holding_card_list) == 0:
            winner = 2
            break
        input()

    print("게임 종료")
    # 무승부시 페어 수가 많은 사람이 승리
    if winner == 0:
        if len(player1.open_card_list) < len(player2.open_card_list):
            winner = 1
        elif len(player1.open_card_list) > len(player2.open_card_list):
            winner = 2
        else:
            winner = 0

    # 승패 표시
    if winner == 0:
        print("무승부!")
    elif winner == 1:
        print(player1.name, "승리!")
    else:
        print(player2.name, "승리!")


if __name__ == "__main__":
    play_game()
