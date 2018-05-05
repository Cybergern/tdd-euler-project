class Card:
    def __init__(self, value, suit):
        assert value in Hand.ORDER
        assert suit in Hand.SUITS
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return self.value + self.suit

    def __repr__(self):
        return self.__str__()


class Hand:
    ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    SUITS = ["H", "D", "C", "S"]

    def __init__(self, hand):
        self.__cards = self.string_to_hand(hand)

    def get_values(self):
        return [card.value for card in self.__cards]

    def get_suits(self):
        return [card.suit for card in self.__cards]

    def get_counts(self):
        return [self.get_values().count(card.value) for card in self.__cards]

    def to_string(self):
        card_string = ""
        for card in self.__cards:
            card_string += card.value + card.suit + " "
        return card_string.rstrip()

    def string_to_hand(self, hand):
        card_list = hand.split(" ")
        cards = []
        for cardString in card_list:
            cards.append(Card(cardString[0], cardString[1]))
        cards = sorted(cards, key=lambda card: ["".join(self.ORDER).index(c) for c in card.value])
        return cards

    def is_straight(self):
        i = self.ORDER.index(self.__cards[0].value)
        if self.ORDER[i:i + 5] != self.get_values():
            return -1
        return i + 4

    def is_straight_flush(self):
        if self.is_straight() == -1 or self.is_flush() == -1:
            return -1
        i = self.ORDER.index(self.__cards[4].value)
        return i

    def is_royal_straight_flush(self):
        if self.ORDER[-5:] != self.get_values() or self.is_flush() == -1:
            return -1
        return self.ORDER.index("A")

    def is_flush(self):
        if len(set(self.get_suits())) != 1:
            return -1
        i = self.ORDER.index(self.__cards[4].value)
        return i

    def has_pair(self):
        if len(set(self.get_values())) != 4:
            return -1
        i = self.ORDER.index(self.get_values()[self.get_counts().index(2)])
        return i

    def has_two_pairs(self):
        if not (len(set(self.get_values())) == 3 and max(self.get_counts()) == 2):
            return -1, -1
        i, j = self.ORDER.index(self.get_values()[1]), self.ORDER.index(self.get_values()[3])
        return i, j

    def has_three_of_a_kind(self):
        counts = self.get_counts()
        if max(counts) != 3:
            return -1
        i = self.ORDER.index(self.get_values()[counts.index(3)])
        return i

    def has_four_of_a_kind(self):
        counts = self.get_counts()
        if max(counts) != 4:
            return -1
        i = self.ORDER.index(self.get_values()[counts.index(4)])
        return i

    def is_full_house(self):
        counts = self.get_counts()
        if not (sorted(set(counts)) == [2, 3]):
            return -1
        i = self.ORDER.index(self.get_values()[counts.index(3)])
        return i

    def get_x_highest_card(self, rank=1):
        return self.ORDER.index(self.get_values()[-rank])

    def get_results(self):
        return [self.is_royal_straight_flush(), self.is_straight_flush(),
                self.has_four_of_a_kind(), self.is_full_house(), self.is_flush(),
                self.is_straight(), self.has_three_of_a_kind(), self.has_two_pairs()[0],
                self.has_two_pairs()[1], self.has_pair(), self.get_x_highest_card(1),
                self.get_x_highest_card(2), self.get_x_highest_card(3),
                self.get_x_highest_card(4), self.get_x_highest_card(5)]


class Table:
    @staticmethod
    def determine_winner(hand1, hand2):
        i = 0
        hand1_results = hand1.get_results()
        hand2_results = hand2.get_results()
        while i < len(hand1_results):
            if hand1_results[i] > hand2_results[i]:
                return 1
            elif hand1_results[i] < hand2_results[i]:
                return 2
            i += 1
        return 0


class Problem54:
    @staticmethod
    def answer():
        f = open("../resources/poker_54.txt", "r")
        p1_winner = 0
        for line in f:
            hand1 = Hand(line[0:14])
            hand2 = Hand(line[15:29])
            if Table.determine_winner(hand1, hand2) == 1:
                p1_winner += 1
        f.close()
        return p1_winner
