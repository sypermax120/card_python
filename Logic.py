from random import randint

class Card():
    def __init__(self):
        self.all_card = [] # Список зі всіма картами
        self.value_card = [] # Скільки балів за карту
        self.mast = ['H', 'D', 'C', 'S'] # Масть карти (чірва буба хреста піка)
        #self.mast1 = ['\u2665', '\u2666', '\u2663', '\u2660'] # Масть карти (чірва буба хреста піка)

        # Создаємо список з 52 карт
        for i in range(0, 52):
            value_card = str(i % 13) # Всього 13 карт 1 масті(узнаємо кол. балів за карту)

            if value_card == '0':
                value_card = 'K'

            if value_card == '1':
                value_card = 'A'

            if value_card =='11':
                value_card = 'J'

            if value_card == '12':
                value_card = 'Q'

            index = int((i / 13) % 13) # Індекс може бути 0 1 2 3
            self.all_card.append(str(value_card) + self.mast[index])
            self.value_card.append(i % 13)
            self.value_card = [13 if i == 0 else i for i in self.value_card] # Заміняє 0 на 13

    def random_all_card(self):
        '''Створюємо цикл, який вибирає рандомну карту з списку і додає її в новий список, щоб перемішати всі карти'''
        c = []
        v = []
        for i in range(len(self.all_card)):
            i = len(self.all_card)
            i = randint(0, i-1) # Рандомно вибирає індекс карти (-1 щоб не вибрало 58 індекс)
            c.append(self.all_card[i])
            v.append(self.value_card[i])
            self.all_card.pop(i)
            self.value_card.pop(i)
        self.all_card = c
        self.value_card = v

    def print_1_card(self, index):
        print(self.ost_card[index])

    def next_card(self):
        self.index += 1
        if self.index == len(self.ost_card):
            self.index = 0

    def select_card_sum(self, card_1, card_2 = [ ]):
        '''Доробити що після складання карт воно їх видалить, і увидальть їхній бал!!!'''
        #self.card_1 = card_1

        if len(card_1) == 2: #
            if isinstance(self.value_triangle[card_1[0]][card_1[1]], int) and \
                    self.avaliable_card[card_1[0]][card_1[1]] == True and \
                    self.value_triangle[card_1[0]][card_1[1]] == 13: # Чи є бал карти, доступ, == 13
                self.card_triangle[card_1[0]][card_1[1]] = 'test'
                self.value_triangle[card_1[0]][card_1[1]] = None
                print('13')

        if len(card_1) == 2 and len(card_2) == 2:
            if isinstance(self.value_triangle[card_1[0]][card_1[1]], int) and \
                    isinstance(self.value_triangle[card_2[0]][card_1[1]], int) and \
                    self.avaliable_card[card_1[0]][card_1[1]] == True and \
                    self.avaliable_card[card_2[0]][card_2[1]] == True and \
                    self.value_triangle[card_1[0]][card_1[1]] + self.value_triangle[card_2[0]][card_2[1]] == 13:
                self.card_triangle[card_1[0]][card_1[1]] = 'test'
                self.value_triangle[card_1[0]][card_1[1]] = None
                self.card_triangle[card_2[0]][card_2[1]] = 'test'
                self.value_triangle[card_2[0]][card_2[1]] = None
                print('13')

        if len(card_1) == 1 and self.ost_value[card_1[0]] == 13:
            del self.ost_card[card_1[0]]
            del self.ost_value[card_1[0]]
            self.index -= 1
            print('13')

        if len(card_1) == 1 and len(card_2) == 2:
            if isinstance(self.value_triangle[card_2[0]][card_2[1]], int) and \
                    self.ost_value[card_1[0]] + self.value_triangle[card_2[0]][card_2[1]] == 13:
                    self.card_triangle[card_2[0]][card_2[1]] = 'test'
                    self.value_triangle[card_2[0]][card_2[1]] = None
                    del self.ost_card[card_1[0]]
                    del self.ost_value[card_1[0]]
                    self.index -= 1
                    print("13")

        if len(card_1) == 2 and len(card_2) == 1:
            if isinstance(self.value_triangle[card_1[0]][card_1[1]], int) and \
                    self.ost_value[card_2[0]] + self.value_triangle[card_1[0]][card_1[1]] == 13:
                    self.card_triangle[card_1[0]][card_1[1]] = 'test'
                    self.value_triangle[card_1[0]][card_1[1]] = None
                    del self.ost_card[card_2[0]]
                    del self.ost_value[card_2[0]]
                    self.index -= 1
                    print("13")

        self.set_avaliable()

    def card_triangl(self):
        self.card_triangle = [[],[],[],[],[],[],[]]
        self.value_triangle = [[],[],[],[],[],[],[]]
        self.avaliable_card = [[], [], [], [], [], [], []] # Змінна з доступними картами
        self.index = 0
        a = 0
        c = 0
        for i in range(1,8):
            for j in range(i):
                self.card_triangle[a] += [self.all_card[c]]
                self.value_triangle[a] += [self.value_card[c]]

                if i < 7:
                    self.avaliable_card[a] += [False]
                else:
                    self.avaliable_card[a] += [True]
                c += 1
            a += 1
        self.ost_card = self.all_card[28:]     # Список зі всіма картами
        self.ost_value = self.value_card[28:]  # Скільки балів за карту

    def print_triangl(self):
        n = 30
        for i in range(len(self.card_triangle)):
            print(n*' ', end='')
            print(self.card_triangle[i]) # self.avaliable_card[i], self.value_triangle[i]
            n-=5
        print(30 * '___')

    def set_avaliable(self):
        '''Буде давати доступ до карти, коли 2 нижных нема'''
        for i in range(1, 7):
            for j in range(i):
                if self.value_triangle[i][j] == None and self.value_triangle[i][j+1] == None:
                    self.avaliable_card[i-1][j] = True

'''a = Card()
a.random_all_card()
a.card_triangl()
a.select_card()
'''