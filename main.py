import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Draw_circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.color = QColor(255, 255, 0)  # Жёлтый цвет

        self.btn.clicked.connect(self.parametrs)

    def parametrs(self):
        self.radius = randint(1, 300)
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw is True:
            painter = QPainter(self)
            painter.setBrush(self.color)
            center_x, center_y = (self.width() // 2, self.height() // 2)
            painter.drawEllipse(center_x - self.radius, center_y - self.radius, 2 * self.radius, 2 * self.radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Draw_circle()
    window.show()
    sys.excepthook = Draw_circle
    sys.exit(app.exec())

