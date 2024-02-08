class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        self.holding_card_list.append(card_list)

    def display_two_card_lists(self):
        print(f'[{self.name}] Open card List: {len(self.open_card_list)}')
        for i in range(len(self.open_card_list)):
            print(self.open_card_list[i], end=' ' if i % 13 != 12 else '\n')

    def check_one_pair_card(self):
        card_list = sorted(self.holding_card_list, key=lambda x: x[1])
        def pair_check(card_list):
            if len(card_list) <= 1:
                return 0
            card1 = card_list[0]
            for card2 in card_list[1:]:
                if card1[1] == card2[1]:
                    self.open_card_list.append(card1)
                    self.open_card_list.append(card2)
                    card_list.remove(card1)
                    card_list.remove(card2)
            if card_list[0] == card1:
                pair_check(card_list[1:])
            else:
                pair_check(card_list)
        pair_check(card_list)
