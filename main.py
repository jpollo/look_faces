import sys
from PyQt4 import QtGui
from win import Ui_MainWindow

app = QtGui.QApplication(sys.argv)

mwin = QtGui.QMainWindow()

ui = Ui_MainWindow()

ui.setupUi(mwin)

mwin.show()
sys.exit(app.exec_())
