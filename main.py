# coding: utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *
from win import Ui_MainWindow
import detect

class Face(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #add button funtion
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.file_open)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.detect)
    
    def file_open(self):
        self.pic_file = QFileDialog.getOpenFileName(self,"Open file dialog","/home/arch","Picture files(*.png *.jpg *.bmp)")
        print self.pic_file
        #filename ----->文件的整个路径
        self.pic = QPixmap(self.pic_file)
        self.pic.scaled(100, 100)
        scene = QGraphicsScene()
        scene.addPixmap(self.pic)
        self.ui.graphicsView.setScene(scene)
    

    def detect(self):
        print self.pic_file
        detect.detectObject(str(self.pic_file))
        #load to show after dected
        self.pic = QPixmap(QString("face1.jpg"))
        self.pic.scaled(100, 100)
        scene = QGraphicsScene()
        scene.addPixmap(self.pic)
        self.ui.graphicsView.setScene(scene)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Face()
    myapp.show()
    sys.exit(app.exec_())

