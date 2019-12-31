# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Hide Window Title
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        self.setCursor(Qt.CrossCursor)
        self.screenWidth = QDesktopWidget().screenGeometry().width()
        self.screenHeight = QDesktopWidget().screenGeometry().height()

        # Shortcut
        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def exitEvent(self):
        exit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(Qt.CrossCursor)

    def shortcutMoveEvent(self, direction):
        if direction == 'left':
            self.move(QPoint(0, self.pos().y()))
        elif direction == 'right':
            self.move(QPoint(self.screenWidth-self.width(), self.pos().y()))
        elif direction == 'up':
            self.move(QPoint(self.pos().x(), 0))
        elif direction == 'down':
            self.move(QPoint(self.pos().x(), self.screenHeight-self.height()))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
