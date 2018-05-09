# -*- coding:utf-8 -*-
# __author__:Arvin.He
import sys
from PyQt5 import QtWidgets

from app.maindlg import MainDialog


app = QtWidgets.QApplication(sys.argv)



if __name__ == "__main__":
    mainDlg = MainDialog()
    mainWinRect = mainDlg.geometry()
    mainDlg.setFixedSize(mainWinRect.size())
    mainDlg.exec_()