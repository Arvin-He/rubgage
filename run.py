# -*- coding:utf-8 -*-
# __author__:Arvin.He
import sys
from PyQt5 import QtWidgets

from app.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)



if __name__ == "__main__":
    mainWindow = MainWindow()
    sys.exit(app.exec_())
