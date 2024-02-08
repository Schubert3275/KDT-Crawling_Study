from math import factorial

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        """카드 추가"""
        self.holding_card_list.append(card_list)

    def display_hand_card_list(self):
        """한 줄에 13개 카드 표시: 손패"""
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')

        for i in range(len(self.holding_card_list)):
            print(self.holding_card_list[i], end=' ' if i % 13 != 12 else '\n')
        print('\n')

    def display_two_card_lists(self):
        """한 줄에 13개 카드 표시: 페어"""
        print('=' * 100)
        print(f'[{self.name}] Open card List: {len(self.open_card_list)}')

        for i in range(len(self.open_card_list)):
            print(self.open_card_list[i], end=' ' if i % 13 != 12 else '\n')
        print('\n')

    def check_one_pair_card(self):
        """재귀호출로 카드 숫자 검사"""
        print('=' * 100)
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')

        card_list = sorted(self.holding_card_list, key=lambda x: x.split(',')[1])

        def pair_check(card_list):
            card1 = card_list[0]  # 리스트의 첫번째 카드를 기준으로 검사
            for card2 in card_list[1:]:
                if card1.split(',')[1] == card2.split(',')[1]:
                    # 카드의 숫자가 일치하면 카드를 open_card_list에 추가하고 holding_card_list에서 삭제
                    self.open_card_list.append(card1)
                    self.open_card_list.append(card2)
                    self.holding_card_list.remove(card1)
                    self.holding_card_list.remove(card2)
                    card_list = sorted(self.holding_card_list, key=lambda x: x.split(',')[1])
                    break
            if card1 == card_list[0]:  # 첫번째 카드와 일치하는 카드가 없으면 첫번째 카드를 제외
                card_list = card_list[1:]
            if len(card_list) <= 1:  # 검사할 카드 숫자가 1개 이하가 되면 종료
                return 0
            pair_check(card_list)  # 재귀호출

        pair_check(card_list)
