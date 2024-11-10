import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI App")
        self.setWindowIcon(QIcon('PyQt5 GUI/icon.jpg'))
        self.setGeometry(500, 300, 1000, 500)
        
        label = QLabel("Welcome To Biratnagar", self)
        label.setFont(QFont('Arial Black', 30))
        label.setGeometry(0,0,1000,200)
        label.setStyleSheet("color: #450c08;"
                            "background-color: #f7f7e1;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop)       #VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom)    #VERTICALLY BOTTOM 
        # label.setAlignment(Qt.AlignVCenter)   #VERTICALLY CENTER
        # label.setAlignment(Qt.AlignRight)     #HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignLeft)      #HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter)   #HORIZONTALLY CENTER
        
        # label.setAlignment(Qt.AlignTop | Qt.AlignRight)       #TOP AND RIGHT
        # label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)     #BOTTOM AND LEFT
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   #CENTER AND CENTER
        label.setAlignment(Qt.AlignCenter)   
        
        
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    