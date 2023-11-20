import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUI('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.paint = False

    def run(self):
        self.paint = True
        self.update()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
        # Начинаем процесс рисования
            qp.begin(self)
            self.draw_cicrle(qp)
        # Завершаем рисование
            qp.end()

    def draw_cicrle(self, qp):
        qp.setBrush(QColor('yellow'))
        w, h = self.geometry().width(), self.geometry().height()
        x, y = random.randrange(0, w - 20), random.randrange(0, h - 20)
        d = random.randrange(10, w - 30)
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
