# -*- coding:utf-8 -*-
# __author__:Arvin.He

import os
import time
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QDialog, QMainWindow, QAction, QLabel
from PyQt5.QtGui import QIcon
from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.initUI()
        self.setGeometry(200, 100, 1024, 768)
        self.show()


    def initUI(self):
        exitAction = QAction(QIcon("C:/Users/jun.he/Pictures/images/cat/5.jpg"), '&退出', self)
        # 设置快捷键
        exitAction.setShortcut('Ctrl+Q')
        # 设置状态栏显示tip
        exitAction.setStatusTip('退出应用')
        exitAction.triggered.connect(self.close)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAction)
        toolbar = self.addToolBar('EXIT')
        toolbar.addAction(exitAction)
        self.listWidget.setFixedWidth(180)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.listWidget.currentItemChanged.connect(self.changePage)
        # self.listWidget.currentRowChanged.connect(self.on_listWidget_currentRowChanged)

        self.tabs = ["主页", "测试", "分析1", "分析2", "设置"]
        for i, name in enumerate(self.tabs):
            item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(item)
            page = QtWidgets.QDialog()

            # page = QtWidgets.QWidget()
            self.stackedWidget.addWidget(page)
        self.listWidget.setCurrentRow(0)

        self.setStyleSheet(
            "QListWidget:item:selected{background-color:forestgreen; color: white;}"
            "QListWidget:item{height: 50px; text-align: center;}")
