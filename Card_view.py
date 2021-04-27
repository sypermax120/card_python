from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from Logic import Card
import cat

class view(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi("GUI.ui",self)
        self.setWindowTitle("CARD")
        self.show()
        self.a = Card() #Перемінна з логікою карт
        self.a.random_all_card()
        self.a.card_triangl()

        self.ui.next_btn.clicked.connect(self.btn_next)

        self.path = "./cards/"
        self.create_field()
        self.update_board()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(0xcbad00))) # 0xbbada0
        painter.drawRect(self.rect())

    def check_sum(self, pos):
        #card_pos = self.sender().position
        '''
        Потрібно в методі зробити так, щоб можна було обробляти 1 або 2 карти
        Вибрати 1 або 2 карти і якщо 13 то видалить
        '''
        if len(self.is_card) < 2:
            self.is_card.append(pos)
            self.a.select_card_sum(self.is_card[0])

        if len(self.is_card) == 2:
            self.a.select_card_sum(self.is_card[0], self.is_card[1])
            self.is_card = []
        print(self.a.card_triangle)
        self.close_label()
        self.update_board()
        print(self.is_card)
        print(self.a.index, self.a.ost_card)

    def btn_next(self):
        self.a.next_card()
        #self.add_card.setText(str(self.a.ost_card[self.a.index]))
        self.add_card.setPixmap(QPixmap(self.path + self.a.ost_card[self.a.index] + '.jpg').scaled(60, 85))

    def create_field(self):
        self.card_field = [[], [], [], [], [], [], []] # наші label
        self.is_card = []
        a = 1
        for i in range(1, len(self.a.card_triangle) + 1):
            for j in range(i):
                self.card_field[i-1] += [eval('self.ui.label_' + str(a))] #Створює наші лейбли і додає їх в список
                #self.card_field[i-1][j].clicked.connect(lambda: self.test([i-1,j])) #Робимо так щоб можна клікати на карти
                a += 1

        self.ui.add_card.clicked.connect(lambda: self.check_sum([self.a.index])) #Клікати на карту з колоди

        self.card_field[0][0].clicked.connect(lambda: self.check_sum([0, 0]))

        self.card_field[1][0].clicked.connect(lambda: self.check_sum([1, 0]))
        self.card_field[1][1].clicked.connect(lambda: self.check_sum([1, 1]))

        self.card_field[2][0].clicked.connect(lambda: self.check_sum([2, 0]))
        self.card_field[2][1].clicked.connect(lambda: self.check_sum([2, 1]))
        self.card_field[2][2].clicked.connect(lambda: self.check_sum([2, 2]))

        self.card_field[3][0].clicked.connect(lambda: self.check_sum([3, 0]))
        self.card_field[3][1].clicked.connect(lambda: self.check_sum([3, 1]))
        self.card_field[3][2].clicked.connect(lambda: self.check_sum([3, 2]))
        self.card_field[3][3].clicked.connect(lambda: self.check_sum([3, 3]))

        self.card_field[4][0].clicked.connect(lambda: self.check_sum([4, 0]))
        self.card_field[4][1].clicked.connect(lambda: self.check_sum([4, 1]))
        self.card_field[4][2].clicked.connect(lambda: self.check_sum([4, 2]))
        self.card_field[4][3].clicked.connect(lambda: self.check_sum([4, 3]))
        self.card_field[4][4].clicked.connect(lambda: self.check_sum([4, 4]))

        self.card_field[5][0].clicked.connect(lambda: self.check_sum([5, 0]))
        self.card_field[5][1].clicked.connect(lambda: self.check_sum([5, 1]))
        self.card_field[5][2].clicked.connect(lambda: self.check_sum([5, 2]))
        self.card_field[5][3].clicked.connect(lambda: self.check_sum([5, 3]))
        self.card_field[5][4].clicked.connect(lambda: self.check_sum([5, 4]))
        self.card_field[5][5].clicked.connect(lambda: self.check_sum([5, 5]))

        self.card_field[6][0].clicked.connect(lambda: self.check_sum([6, 0]))
        self.card_field[6][1].clicked.connect(lambda: self.check_sum([6, 1]))
        self.card_field[6][2].clicked.connect(lambda: self.check_sum([6, 2]))
        self.card_field[6][3].clicked.connect(lambda: self.check_sum([6, 3]))
        self.card_field[6][4].clicked.connect(lambda: self.check_sum([6, 4]))
        self.card_field[6][5].clicked.connect(lambda: self.check_sum([6, 5]))
        self.card_field[6][6].clicked.connect(lambda: self.check_sum([6, 6]))

    def update_board(self):
        '''Відображає картинки в нашому вікні програми'''
        self.ui.add_card.setPixmap(QPixmap(self.path + self.a.ost_card[self.a.index] + '.jpg').scaled(60, 85))
        #self.add_card.setText(str(self.a.ost_card[self.a.index]))
        for i in range(len(self.a.card_triangle)):
            for j in range(len(self.a.card_triangle[i])):
                card = self.a.card_triangle[i][j]
                if self.a.avaliable_card[i][j] == False:
                    self.card_field[i][j].setPixmap(QPixmap(self.path + 'back' + '.jpg').scaled(60, 85))
                else:
                    self.card_field[i][j].setPixmap(QPixmap(self.path + card + '.jpg').scaled(60, 85))
                #self.card_field[i][j].setText(str(self.a.card_triangle[i][j]))

    def close_label(self):
        for i in range(len(self.a.card_triangle)):
            for j in range(i):
                if self.a.card_triangle[i][j] == "test":
                    pass
                    #self.card_field[i][j].close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = view()
    sys.exit(app.exec())
