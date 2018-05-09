# -*- coding:utf-8 -*-
# __author__:Arvin.He

import os
import time
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon("C:/Users/jun.he/Pictures/images/cat/5.jpg"), '&退出', self)
        # 设置快捷键
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用')
        exitAction.triggered.connect(self.close)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAction)
        toolbar = self.addToolBar('EXIT')
        toolbar.addAction(exitAction)

        self.setGeometry(200, 100, 1024, 768)
        self.show()

