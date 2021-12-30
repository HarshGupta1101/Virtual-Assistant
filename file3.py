#from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate ,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from file2 import Ui_MainWindow
import file1
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.taskexecution
   
    

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1=QMovie("element_jarvis.gif")
        self.gui.label.setMovie(self.gui.label1)
        self.gui.label1.start()
        
        startExecution.start()
      
        
guiapp=QApplication(sys.argv)
var=Main()
var.show()
sys.exit(guiapp.exec_())    