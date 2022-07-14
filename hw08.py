class Card:
    SUITS = ['S', 'H', 'D', 'C']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    SUIT_CNT = len(SUITS)
    RANK_CNT = len(RANKS)
    CARD_CNT = SUIT_CNT * RANK_CNT
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit + Card.RANKS[self.rank - 1]

# 定義玩家類別
class Player:
    def __init__(self, name):
        self.name = name
        self.card_list = []

    def draw_a_card(self, card):
        self.card_list.append(card)

    def is_four_of_a_kind(self):  # 判斷是否為鐵支
        foak = False
        f_rank = [card.rank for card in self.card_list]
        set_card = set(f_rank)
        for r in set_card:
            if f_rank.count(r) == 4:
                foak = True
                break
        return foak    
    
    def is_full_house(self):
        full_house = False
        f_rank = [card.rank for card in self.card_list]
        set_card = set(f_rank)
        # 如果剛好兩種數字，但不是鐵支
        if len(set_card) == 2 and self.is_four_of_a_kind() == False:
            full_house = True
        return full_house

    def is_straight(self): # 判斷是否為順子
        straight = True
        s_rank = []
        for card in self.card_list:
            s_rank.append(card.rank)
        sorted_rank = sorted(s_rank)
        # 正規判斷法 (ex: 5,6,7,8,9)
        for i in range(len(sorted_rank)):
            try:
                if sorted_rank[i] + 1 != sorted_rank[i+1]:
                    straight = False
                    break
            except IndexError:
                break
        # 奇怪規則 (ex: 1,2,11,12,13)
        if sorted_rank == [1,10,11,12,13] or sorted_rank == [1,2,11,12,13] or\
            sorted_rank == [1,2,3,12,13] or sorted_rank == [1,2,3,4,13]:
            straight = True                
        return straight
        

    def is_flush(self): # 判斷是否為同花
        flush = True
        the_flush = self.card_list[0].suit
        for card in self.card_list:
            if card.suit != the_flush:
                flush = False
                break
        return flush
    
    def is_three_of_a_kind(self):
        toak = False
        t_rank = [card.rank for card in self.card_list]
        set_card = set(t_rank)
        if len(set_card) == 3:
            for r in set_card:
                if t_rank.count(r) == 3:
                    toak = True
        return toak

    def is_two_pairs(self):
        two_pairs = False
        t_rank = [card.rank for card in self.card_list]
        set_card = set(t_rank)
        if len(set_card) == 3 and self.is_three_of_a_kind() == False:
            two_pairs = True
        return two_pairs

    def is_one_pair(self):
        one_pair = False
        t_rank = [card.rank for card in self.card_list]
        set_card = set(t_rank)
        if len(set_card) == 4:
            one_pair = True
        return one_pair

    def get_rank(self):  # 比大小
        if self.is_straight() and self.is_flush():
            return 1
        elif self.is_four_of_a_kind():
            return 2
        elif self.is_full_house():
            return 3
        elif self.is_flush():
            return 4
        elif self.is_straight():
            return 5
        elif self.is_three_of_a_kind():
            return 6
        elif self.is_two_pairs():
            return 7
        elif self.is_one_pair():
            return 8
        else:
            return 9
    def __str__(self):
        s = self.name + "'s hand: "
        for i in range(len(self.card_list)):
            s += self.card_list[i].suit + str(Card.RANKS[self.card_list[i].rank - 1]) + ','
        return s[:-1]

# input
n_players = int(input())
handcard_list = [[i for i in input().split(',')] for player in range(n_players)]
players = []
players_name = [i for i in input().split(',')]
for i in range(n_players):
    players.append(Player(players_name[i]))

# 發牌
for i in range(n_players):
    for j in range(len(handcard_list[0])):
        suit = handcard_list[i][j][0]
        rank = Card.RANKS.index(handcard_list[i][j][1]) + 1
        players[i].draw_a_card(Card(suit, rank))  # 這裡的players[i]為Player()
    
# 比牌
result = []
for i in range(n_players):
    result.append(players[i].get_rank())
winner_handtype = min(result)
if result.count(winner_handtype) == 1:
    winner = players[result.index(winner_handtype)].name
# 複數贏家
else:
    winner = result.count(winner_handtype)
print(winner)


# for player in range(n_players):
#     print(players[player])


# player1 = Player('Leo')

# player1.draw_a_card(Card('S', 1))
# player1.draw_a_card(Card('F', 2))
# player1.draw_a_card(Card('S', 2))
# player1.draw_a_card(Card('S', 2))
# player1.draw_a_card(Card('S', 13))
# # print(player1.card_list)
# print('順子: ', player1.is_straight())
# print('同花: ', player1.is_flush())
# print('鐵支: ', player1.is_four_of_a_kind())
# print('葫蘆: ', player1.is_full_house())
# print('三條: ', player1.is_three_of_a_kind())
# print('兩對: ', player1.is_two_pairs())
# print('一對: ', player1.is_one_pair())
# print(player1.get_rank())
# print(player1)