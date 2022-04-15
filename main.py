from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.exitAct = QAction(QIcon("exit.png"), 'Exit', self)
        self.exitAct.setStatusTip("Exit")
        self.exitAct.triggered.connect(qApp.quit)
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('File')
        self.helpMenu = self.menubar.addMenu('Home')
        self.fileMenu.addAction(self.exitAct)
        #Pages
        self.page1 = Window("Page1")
        self.page2 = Window("Page2")
        self.page3 = Window("Page3")
        self.page4 = Window("Page4")
        #Page tracker
        self.page_tracker = [self.page1,self.page2,self.page3,self.page4]
        self.setCentralWidget(self.page1)
        self.setGeometry(200, 300, 600, 600)


        #Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.forward = QPushButton("Forward")
        self.backward = QPushButton("Backward")
        self.status_bar.addWidget(self.backward)
        self.status_bar.addWidget(self.forward)
        self.show()
    def change_page(self,dir):
        pass

class Window(QWidget):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.label = QLabel(self.name,self)

def run_program():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = Main_Window()
    app.exec()
if __name__ == '__main__':
    run_program()

