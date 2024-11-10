import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 1000, 800)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(400, 300, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        
        self.label.setGeometry(400, 400, 250, 100)
        self.label.setStyleSheet("font-size: 50px;")
        
    def on_click(self):
        print("Button Clicked.")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.button.setStyleSheet("background-color: #90cef5;"
                                  "font-size: 30px;"
                                  "color: #167a1b")
        self.label.setText("GoodByee")
        
        
        
        
       
        
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        