# -*- coding:utf-8 -*-
# __author__:Arvin.He

import os
import time
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .maindlg_ui import Ui_mainDlg


class MainDialog(QDialog, Ui_mainDlg):

    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint |
                            Qt.WindowCloseButtonHint)
        self.initUI()


    def initUI(self):
        self.show()

