class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        for card in card_list:
            self.holding_card_list.append(card)

    def add_card(self, card):
        self.holding_card_list.append(card)

    def display_two_card_lists(self):
        print('=' * 60)

        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        for card in self.open_card_list:
            print(card, end=' ')
        print()
        print()

        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        for card in self.holding_card_list:
            print(card, end=' ')
        print()
        print()

    def check_one_pair_card(self):
        print('=' * 60)
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')
        for i in range(0, len(self.holding_card_list) - 1):
            card1 = self.holding_card_list[i]
            for j in range(i + 1, len(self.holding_card_list)):
                card2 = self.holding_card_list[j]
                if card1.number == card2.number:
                    if card1 not in self.open_card_list and card2 not in self.open_card_list:
                        self.open_card_list.append(card1)
                        self.open_card_list.append(card2)

        # open_card_list에 저장한 항목들을 holding_card_list에서 제거
        for card in self.open_card_list:
            if card in self.holding_card_list:
                self.holding_card_list.remove(card)

        self.display_two_card_lists()

    def get_holding_card_count(self):
        return len(self.holding_card_list)

    def get_open_card_count(self):
        return len(self.open_card_list)
