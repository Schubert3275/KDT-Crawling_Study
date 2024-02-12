from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")

    dealer = GameDealer()

    # GameDealer가 한 벌의 카드 생성
    dealer.make_deck()

    # 초기 10장의 카드를 나누어 주고, 각 player들은 자신이 가지고 있는 카드 목록을 출력
    card_list1, card_list2 = dealer.distribute_card(10)
    player1.add_card_list(card_list1)
    player1.display_two_card_lists()

    player2.add_card_list(card_list2)
    player2.display_two_card_lists()

    #---------------------------------------------------------------
    # 5 단계
    # ---------------------------------------------------------------
    step = 1;
    key = input(f'[{step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요! ')
    while (True):
        player1.check_one_pair_card()
        player2.check_one_pair_card()

        player1_holdingcard_count = player1.get_holding_card_count()
        player2_holdingcard_count = player2.get_holding_card_count()

        if player1_holdingcard_count == 0 or player2_holdingcard_count == 0 or len(dealer.deck) == 0:
            break

        step += 1
        key = input(f'[{step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요! ')

        if len(dealer.deck) > 0:
            card_list1, card_list2 = dealer.distribute_card(4)  # 매회 4장의 카드를 나누어줌
            player1.add_card_list(card_list1)
            player2.add_card_list(card_list2)

    print()

def play_game_test():
    '''
        One pair 카드 검사 기능 테스트 함수
    :return:
    '''
    player1 = Player("흥부")

    # case #1: 번호가 같은 카드가 4장 존재
    player1.add_card(Card('♠', '2'))
    player1.add_card(Card('♥', '2'))
    player1.add_card(Card('♣', '2'))
    player1.add_card(Card('◆', '2'))
    player1.add_card(Card('◆', '3'))
    player1.display_two_card_lists()

    key = input('다음 단계 진행을 위해 Enter 키를 누르세요! ')
    player1.check_one_pair_card()
    player1.display_two_card_lists()

    key = input('다음 단계 진행을 위해 Enter 키를 누르세요! ')
    player1.add_card(Card('♠', 'K'))
    player1.add_card(Card('♥', 'K'))
    player1.add_card(Card('◆', '4'))
    player1.add_card(Card('◆', 'K'))
    player1.check_one_pair_card()
    player1.display_two_card_lists()

    #card_suits = ["♠", "♥", "♣", "◆"]
    #card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

if __name__ == '__main__':
    play_game()
    #play_game_test()
