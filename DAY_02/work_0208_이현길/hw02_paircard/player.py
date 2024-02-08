class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        self.holding_card_list.append(card_list)

    def display_hand_card_list(self):
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')

        for i in range(len(self.holding_card_list)):
            print(self.holding_card_list[i], end=' ' if i % 13 != 12 else '\n')
        print('\n')

    def display_two_card_lists(self):
        print('=' * 100)
        print(f'[{self.name}] Open card List: {len(self.open_card_list)}')

        for i in range(len(self.open_card_list)):
            print(self.open_card_list[i], end=' ' if i % 13 != 12 else '\n')
        print('\n')

    def check_one_pair_card(self):
        print('=' * 100)
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')

        count = (len(self.holding_card_list))**2
        card_list = self.holding_card_list

        def pair_check(card_list, count):
            if count == 0:
                return 0
            count -= 1
            card1 = card_list[0]
            for card2 in card_list[1:]:
                if card1.split(',')[1] == card2.split(',')[1]:
                    self.open_card_list.append(card1)
                    self.open_card_list.append(card2)
                    self.holding_card_list.remove(card1)
                    self.holding_card_list.remove(card2)
                    card_list = self.holding_card_list
                    break
            if len(card_list) <= 1:
                return 0
            if card1 == card_list[0]:
                card_list = card_list[1:]
            pair_check(card_list, count-1)

        pair_check(card_list, count)
