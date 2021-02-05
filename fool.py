import random
from enum import Enum



class Card(object):

    # масти
    spades = '♠'
    hearts = '♥'
    diamonds = '♦'
    clubs = '♣'
    noms = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # достоинтсва карт
    noms_short = ['J', 'Q', 'K', 'A']

    value = {n: i for i, n in enumerate(noms)}  # поиск индекса по достоинству
    cards_in_hand_max = 6  # карт в руке при раздаче

    # эталонная колода (каждая масть по каждому номиналу) - 36 карт
    DECK = [(nom, suit) for nom in noms for suit in [spades, hearts, diamonds, clubs]]
    # print(DECK)

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        self.suit = str
        return str(crit.hunger) + "\n" + str(crit.boredom)

    def __repr__(self):
        pass

    def __lt__(self):
        pass

    def __eq__(self):
        pass

# а) в конструкторе наполнение полной колодой или картами из конструктора
# б) метод перемешивания колоды, метод извлечения случайной карты
# в) метод b__str__ для вывода на экран

class CardDeck(self):
    def __init__(self, cards=None):
        if cards is None:
            self._cards = self._get_full_deck()
        else:
            self._cards = cards

    def __str__(self):
        '''
        String representation of Deck
        '''

    def shuffle(self):
        '''
        Randomly shuffle cards in deck
        '''
        pass

    def pick_first(self):
        '''
        remove first card in dec and return it
        '''
        pass

    def _get_full_deck(self):
        '''
        Generate list of 36 cards
        '''
        pass

class Deck:
    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.ranks = list(range(2, 15))
        self.cards_list = []
        self.uber = None
        self.top_card = None
        self.build()

    def build(self):
        for s in self.suits:
            for r in self.ranks:
                self.cards_list.append(Card(r, s))
        self.shuffle()
        self.flip_top_card()

    def flip_top_card(self):
        # To be called at the start of the game, before cards are dealt
        self.top_card = self.pop()
        self.uber = self.top_card.suit
        for c in self.cards_list:
            c.uber = self.uber
        self.cards_list.insert(0, self.top_card)

    def shuffle(self):
        shuffle(self.cards_list)

    def pop(self):
        return self.cards_list.pop()

    def __len__(self):
        return len(self.cards_list)

    def __str__(self):
        return "Deck has {} cards left".format(len(self.cards_list))

# 3. Функцию начала игры в дурака
    # а) чтение с клавиатуры кол - ва игроков.
    # б) используя класс из 2. случайно раздать игрокам колоды по 6 карт
    # в) случайно выбрать одну карту из колоды как козырь
    # г) определить кто ходит первым, вывести колоды игроков на экран

class Player:
    def __init__(self, index, cards):
        self.index = index
        self.cards = list(map(tuple, cards))  # убедимся, что будет список кортежей

    def take_cards_from_deck(self, deck: list):
        """
        Взять недостающее количество карт из колоды
        Колода уменьшится
        :param deck: список карт колоды
        """
        lack = max(0, cards_in_hand_max - len(self.cards))
        n = min(len(deck), lack)
        self.add_cards(deck[:n])
        del deck[:n]
        return self

    def sort_hand(self):
        """
        Сортирует карты по достоинству и масти
        """
        self.cards.sort(key=lambda c: (NAME_TO_VALUE[c[0]], c[1]))
        return self

    def add_cards(self, cards):
        self.cards += list(cards)
        self.sort_hand()
        return self

    # всякие вспомогательные функции:

    def __repr__(self):
        return f"Player{self.cards!r}"

    def take_card(self, card):
        self.cards.remove(card)

    @property
    def n_cards(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def get_player_deck(card_deck):
        '''
        Using Full deck create deck for particular player
        '''
        pass


    def print_players(players):
        '''
        Print players decks to screen
        '''
        pass


    def get_first_player(players, trump):
        '''
        Select player who will play frist
        '''
        pass


    def main():
        full_deck = CardDeck()
        # Ввод количества игроков, не более 6-ти
        num_players = int(input('Enter num players'))
        players = [get_player_deck(full_deck) for i in range(num_players)]
        print_players(player)
        trump =
        first_player = get_first_player(players, trump)

